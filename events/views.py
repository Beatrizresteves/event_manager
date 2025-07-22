from .models import Event, Participant
from .serializers import EventSerializer, ParticipantSerializer, EventReportSerializer
from event_manager.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, permissions, filters
from rest_framework.exceptions import ValidationError
from .tasks import enviar_email_inscricao_confirmada
from rest_framework import generics

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET' and self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated(), IsOwnerOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['event__id']

    def perform_create(self, serializer):
        user = self.request.user
        event = serializer.validated_data['event']

        if Participant.objects.filter(user=user, event=event).exists():
            raise ValidationError("Você já está inscrito neste evento.")

        serializer.save(user=user)
        enviar_email_inscricao_confirmada.delay(user.email, event.title)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Participant.objects.filter(user=user)
        return Participant.objects.none()
class EventReportListView(generics.ListAPIView):
    queryset = Event.objects.prefetch_related('participants__user')
    serializer_class = EventReportSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Event.objects.prefetch_related('participants__user')
        print('EVENTOS:', list(queryset))  
        return queryset
    
class EventReportView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventReportSerializer

    def get_queryset(self):
        print("ENTROU NO GET_QUERYSET")
        user = self.request.user
        print("USUÁRIO:", user)

        queryset = Event.objects.filter(participants__user=user).distinct()
        print("QUERYSET:", queryset)
        return queryset
