from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class IndexViewTest(TestCase):

    def setUp(self):
        self.url = reverse('common:index')
        self.HTTP_200_OK = 200

    def login_with_session_authentication(self):
        User.objects.create_user('test', 'test@test.com', 'test_password')
        self.client.login(username='test', password='test_password')

    def test_get_index_view_without_authentication_provided(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, self.HTTP_200_OK,
            'Expected Response Code 200, received {0} instead.'.format(response.status_code))

    def test_get_index_view_with_session_authentication(self):
        self.login_with_session_authentication()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, self.HTTP_200_OK,
            'Expected Response Code 200, received {0} instead.'.format(response.status_code))
