from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class TestProfileView(TestCase):

    def setUp(self):
        self.user_detail_url = reverse('common:profile')

    def test_view_with_valid_user(self):
        test_user = User.objects.create_user('test_username', 'test@test.com', 'test_password')
        self.client.login(username='test_username', password='test_password')
        response = self.client.get(self.user_detail_url)
        response_user = response.context['user']
        self.assertEqual(response_user, test_user,
            'Expected response user to be equals to request user')
