from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Event, Participant

User = get_user_model()

class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ParticipantReportSerializer(serializers.ModelSerializer):
    user = UserBasicSerializer(read_only=True)

    class Meta:
        model = Participant
        fields = ['user']

class EventReportSerializer(serializers.ModelSerializer):
    participants = ParticipantReportSerializer(many=True, read_only=True)
    inscritos_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'inscritos_count', 'participants']

    def get_inscritos_count(self, obj):
        return obj.participants.count()

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'time', 'location'] 
        extra_kwargs = {
            'created_by': {'read_only': True},  
        }

class ParticipantSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username') 

    class Meta:
        model = Participant
        fields = ['id', 'event', 'user', 'registered_at']
