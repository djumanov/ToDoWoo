from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Todo


class TodoTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)
        self.todo_data = {
            'title': 'Test Todo',
            'memo': 'Test memo',
        }

    def test_todo_create_view(self):
        url = reverse('todo_create')
        response = self.client.post(url, self.todo_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().title, 'Test Todo')
        self.assertEqual(Todo.objects.get().user, self.user)

    def test_todo_create_view_unauthenticated(self):
        self.client.force_authenticate(user=None)
        url = reverse('todo_create')
        response = self.client.post(url, self.todo_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Todo.objects.count(), 0)

    def test_todo_detail_view(self):
        todo = Todo.objects.create(
            title='Test Todo',
            memo='Test memo',
            user=self.user
        )
        url = reverse('todo_detail', args=[todo.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Todo')
        self.assertEqual(response.data['user'], self.user.id)

    def test_todo_detail_view_unauthenticated(self):
        todo = Todo.objects.create(
            title='Test Todo',
            memo='Test memo',
            user=self.user
        )
        self.client.force_authenticate(user=None)
        url = reverse('todo_detail', args=[todo.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
