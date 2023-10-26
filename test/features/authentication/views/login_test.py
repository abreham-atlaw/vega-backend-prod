from django.test import TestCase, Client
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from features.authentication.models import VegaUser


class LoginViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = VegaUser.objects.create_user(username='testuser', password='testpassword')

    def test_login_success(self):
        response = self.client.post('/api/auth/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertTrue('token' in response.data)
        token = Token.objects.get(user=self.user)
        self.assertEqual(response.data['token'], token.key)

    def test_login_failure(self):
        response = self.client.post('/login/', {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)
