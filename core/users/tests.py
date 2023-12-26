from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class SignUpViewTests(APITestCase):
    def setUp(self):
        self.signup_url = reverse('signup')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

    def test_signup_success(self):
        response = self.client.post(self.signup_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.get().username, 'testuser')

    def test_signup_missing_required_fields(self):
        incomplete_data = {
            'username': 'testuser',
        }

        response = self.client.post(self.signup_url, incomplete_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(get_user_model().objects.count(), 0)

    def test_signup_existing_user(self):
        get_user_model().objects.create_user(username='testuser', password='testpassword')

        response = self.client.post(self.signup_url, self.user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(get_user_model().objects.count(), 1)
