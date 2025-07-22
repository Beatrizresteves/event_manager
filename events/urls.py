from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ParticipantViewSet, EventReportListView

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'participants', ParticipantViewSet, basename='participant')

urlpatterns = [
    path('reports/events/', EventReportListView.as_view(), name='event-report-list'),
    path('', include(router.urls)),
]
