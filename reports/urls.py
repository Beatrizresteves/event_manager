from django.urls import path
from .views import EventReportView

urlpatterns = [
    path('events/', EventReportView.as_view(), name='events-report'),
]
