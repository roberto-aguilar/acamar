from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from api import views

class UserTest(APITestCase):

    def setUp(self):
        self.users_url = reverse('user-list')
        self.new_user_data = {
            'username': 'test_username',
            'groups': [],
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test_email@test.com'
        }

    def test_create_user_without_authentication_provided(self):
        response = self.client.post(self.users_url, self.new_user_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED,
            'Expected Response Code 401, received {0} instead.'.format(response.status_code))

    def test_create_user_with_session_authentication(self):
        User.objects.create_user('test', 'test@test.com', 'test_password')
        self.client.login(username='test', password='test_password')
        response = self.client.post(self.users_url, self.new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
            'Expected Response Code 201, received {0} instead.'.format(response.status_code))

    def test_create_user_with_token_authentication(self):
        test_user = User.objects.create_user('test', 'test@test.com', 'test_password')
        token = Token.objects.create(user=test_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(self.users_url, self.new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
            'Expected Response Code 201, received {0} instead.'.format(response.status_code))
