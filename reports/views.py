from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from events.models import Event
from django.db.models import Count

class EventReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Event.objects.annotate(
            total_participants=Count('participants')
        ).values('id', 'title', 'total_participants')
        return Response(data)