from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from api import views

class UserTest(APITestCase):

    def setUp(self):
        self.users_url = reverse('user-list')

    def login_with_session_authentication(self):
        User.objects.create_user('test', 'test@test.com', 'test_password')
        self.client.login(username='test', password='test_password')

    def login_with_token_authentication(self):
        test_user = User.objects.create_user('test', 'test@test.com', 'test_password')
        token = Token.objects.create(user=test_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_users_without_authentication_provided(self):
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED,
            'Expected Response Code 401, received {0} instead.'.format(response.status_code))

    def test_get_users_with_session_authentication(self):
        self.login_with_session_authentication()
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
            'Expected Response Code 200, received {0} instead.'.format(response.status_code))

    def test_get_users_with_token_authentication(self):
        self.login_with_token_authentication()
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
            'Expected Response Code 200, received {0} instead.'.format(response.status_code))

    def test_create_user_without_authentication_provided(self):
        new_user_data = {
            'username': 'test_username',
            'groups': [],
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test_email@test.com'
        }
        response = self.client.post(self.users_url, new_user_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED,
            'Expected Response Code 401, received {0} instead.'.format(response.status_code))

    def test_create_user_with_session_authentication(self):
        self.login_with_session_authentication()
        new_user_data = {
            'username': 'test_username',
            'groups': [],
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test_email@test.com'
        }
        response = self.client.post(self.users_url, new_user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
            'Expected Response Code 201, received {0} instead.'.format(response.status_code))

    def test_create_user_with_token_authentication(self):
        self.login_with_token_authentication()
        new_user_data = {
            'username': 'test_username',
            'groups': [],
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test_email@test.com'
        }
        response = self.client.post(self.users_url, new_user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
            'Expected Response Code 201, received {0} instead.'.format(response.status_code))

    def test_update_user_without_authentication_provided(self):
        test_user = User.objects.create_user('test', 'test@test.com', 'test_password')
        url = self.users_url + '%s/' % test_user.pk
        user_data_to_update =  {
            'username': 'test_username_updated',
            'groups': [],
            'first_name': 'test_first_name_updated',
            'last_name': 'test_last_name_updated',
            'email': 'test_email_updated@test.com'
        }
        response = self.client.put(url, user_data_to_update)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED,
            'Expected Response Code 401, received {0} instead.'.format(response.status_code))

    def test_update_user_with_session_authentication(self):
        self.login_with_session_authentication()
        test_user = User.objects.create_user('test_to_update', 'test_to_update@test.com', 'test_password_to_update')
        url = self.users_url + '%s/' % test_user.pk
        user_data_to_update =  {
            'username': 'test_username_updated',
            'groups': [],
            'first_name': 'test_first_name_updated',
            'last_name': 'test_last_name_updated',
            'email': 'test_email_updated@test.com'
        }
        response = self.client.put(url, user_data_to_update)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
            'Expected Response Code 200, received {0} instead.'.format(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK,
            'Expected Response Code 200, received {0} instead.'.format(response.status_code))
        self.assertEqual(response.data['username'], user_data_to_update['username'],
            'Expected response username "{0}" to be equal to request username "{1}"'.format(
                response.data['username'], user_data_to_update['username']))
        self.assertEqual(response.data['groups'], user_data_to_update['groups'],
            'Expected response groups "{0}" to be equal to request groups "{1}"'.format(
                response.data['groups'], user_data_to_update['groups']))
        self.assertEqual(response.data['first_name'], user_data_to_update['first_name'],
            'Expected response first_name "{0}" to be equal to request first_name "{1}"'.format(
                response.data['first_name'], user_data_to_update['first_name']))
        self.assertEqual(response.data['last_name'], user_data_to_update['last_name'],
            'Expected response last_name "{0}" to be equal to request last_name "{1}"'.format(
                response.data['last_name'], user_data_to_update['last_name']))
        self.assertEqual(response.data['email'], user_data_to_update['email'],
            'Expected response email "{0}" to be equal to request email "{1}"'.format(
                response.data['email'], user_data_to_update['email']))

    def test_update_user_with_token_authentication(self):
        self.login_with_token_authentication()
        test_user = User.objects.create_user('test_to_update', 'test_to_update@test.com', 'test_password_to_update')
        url = self.users_url + '%s/' % test_user.pk
        user_data_to_update =  {
            'username': 'test_username_updated',
            'groups': [],
            'first_name': 'test_first_name_updated',
            'last_name': 'test_last_name_updated',
            'email': 'test_email_updated@test.com'
        }
        response = self.client.put(url, user_data_to_update)
        self.assertEqual(response.status_code, status.HTTP_200_OK,
            'Expected Response Code 200, received {0} instead.'.format(response.status_code))
        self.assertEqual(response.data['username'], user_data_to_update['username'],
            'Expected response username "{0}" to be equal to request username "{1}"'.format(
                response.data['username'], user_data_to_update['username']))
        self.assertEqual(response.data['groups'], user_data_to_update['groups'],
            'Expected response groups "{0}" to be equal to request groups "{1}"'.format(
                response.data['groups'], user_data_to_update['groups']))
        self.assertEqual(response.data['first_name'], user_data_to_update['first_name'],
            'Expected response first_name "{0}" to be equal to request first_name "{1}"'.format(
                response.data['first_name'], user_data_to_update['first_name']))
        self.assertEqual(response.data['last_name'], user_data_to_update['last_name'],
            'Expected response last_name "{0}" to be equal to request last_name "{1}"'.format(
                response.data['last_name'], user_data_to_update['last_name']))
        self.assertEqual(response.data['email'], user_data_to_update['email'],
            'Expected response email "{0}" to be equal to request email "{1}"'.format(
                response.data['email'], user_data_to_update['email']))
