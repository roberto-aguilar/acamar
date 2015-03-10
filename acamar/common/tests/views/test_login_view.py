from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class TestLoginView(TestCase):

    def setUp(self):
        self.login_url = reverse('common:login')

    def test_login_view_with_user_not_authenticated(self):
        HTTP_200_OK = 200
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, HTTP_200_OK,
            'Expected response status code 200, received {status_code} instead.'.format(
                status_code=response.status_code))

    def test_login_view_with_user_authenticated(self):
        user_profile_detail_url = reverse('accounts:user_profile_detail')
        User.objects.create_user('test_username', 'test@test.com', 'test_password')
        self.client.login(username='test_username', password='test_password')
        response = self.client.get(self.login_url)
        self.assertRedirects(response, expected_url=user_profile_detail_url,
            msg_prefix='Expected response redirect to user profile view on already authenticated users')

    def test_login_view_with_authentication_data_provided(self):
        User.objects.create_user('test_username', 'test@test.com', 'test_password')
        user_profile_detail_url = reverse('accounts:user_profile_detail')
        form_data = {
            'username': 'test_username',
            'password': 'test_password'
        }
        response = self.client.post(self.login_url, form_data)
        self.assertRedirects(response, expected_url=user_profile_detail_url,
            msg_prefix='Expected response redirect to user profile view with valid authentication data provided')
