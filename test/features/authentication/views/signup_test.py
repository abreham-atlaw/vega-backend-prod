from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


class SignupViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.signup_url = "/api/auth/signup"

    def test_signup_success(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(username=data['username'])
        self.assertIsNotNone(user)
