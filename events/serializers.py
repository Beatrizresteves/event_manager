from rest_framework import serializers
from .models import Event,Participant

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        extra_kwargs = {
            'created_by': {'read_only': True},  
        }

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'user', 'event', 'registered_at']
        read_only_fields = ['user', 'registered_at']