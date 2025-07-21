from .models import Event, Participant
from .serializers import EventSerializer, ParticipantSerializer
from event_manager.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, permissions, filters
from rest_framework.exceptions import ValidationError
from .tasks import enviar_email_inscricao_confirmada


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

        participant = serializer.save(user=user)

        # Chama a task assíncrona para enviar e-mail de confirmação
        enviar_email_inscricao_confirmada.delay(user.email, event.title)

    def get_queryset(self):
        event_id = self.request.query_params.get('event')
        if event_id:
            return Participant.objects.filter(event__id=event_id)
        return Participant.objects.all()
