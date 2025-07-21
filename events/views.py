from .models import Event
from .serializers import EventSerializer
from event_manager.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, permissions
from .models import Participant
from .serializers import ParticipantSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET' and self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated(), IsOwnerOrReadOnly()]
    
    def perform_create(self, serializer):
        print("Criando participante para usuário:", self.request.user)
        serializer.save(created_by=self.request.user)


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        event = serializer.validated_data['event']

        # Verifica se o usuário já está inscrito
        if Participant.objects.filter(user=user, event=event).exists():
            raise ValidationError("Você já está inscrito neste evento.")

        serializer.save(user=user)
