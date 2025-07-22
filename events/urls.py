# events/urls.py
from django.urls import path, include
from .views import EventReportListView
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ParticipantViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'participants', ParticipantViewSet)

urlpatterns = [
    path('reports/events/', EventReportListView.as_view(), name='event-report-list'), 
]

urlpatterns += router.urls
