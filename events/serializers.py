from rest_framework import serializers
from .models import Event, Participant

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'read_only': True},  
        }

class ParticipantSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username') 

    class Meta:
        model = Participant
        fields = ['id', 'event', 'user', 'registered_at']