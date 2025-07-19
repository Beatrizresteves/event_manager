from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from events.models import Event
from django.urls import reverse


User = get_user_model()

class EventPermissionTests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', 
            email='user1@example.com',
            password='pass1234'
        )
        self.user2 = User.objects.create_user(
            username='user2', 
            email='user2@example.com',
            password='pass1234'
        )

        self.event = Event.objects.create(
            title='Evento do User1',
            description='Descrição',
            location='Local',
            date='2025-07-20',
            time='10:00:00',
            created_by=self.user1
        )

        self.client = APIClient()

    def test_list_events_is_public(self):
        url = reverse('event-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_event_requires_authentication(self):
        url = reverse('event-list')
        data = {
            'title': 'Novo Evento',
            'description': 'Descrição',
            'location': 'Local',
            'date': '2025-07-22',
            'time': '10:00:00',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_event_authenticated(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('event-list')
        data = {
            'title': 'Evento Autenticado',
            'description': 'Descrição',
            'location': 'Local',
            'date': '2025-07-22',
            'time': '10:00:00',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_event_not_owner(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('event-detail', args=[self.event.id])
        data = {
            'title': 'Alterado por user2',
            'description': self.event.description,
            'location': self.event.location,
            'date': self.event.date,
            'time': self.event.time,
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_event_owner(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('event-detail', args=[self.event.id])
        data = {
            'title': 'Alterado por user1',
            'description': self.event.description,
            'location': self.event.location,
            'date': self.event.date,
            'time': self.event.time,
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
