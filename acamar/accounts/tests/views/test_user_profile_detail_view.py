from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class TestUserProfileDetailView(TestCase):

    def setUp(self):
        self.user_profile_detail_url = reverse('accounts:user_profile_detail')

    def create_test_user(self):
        return User.objects.create_user('test_username', 'test@test.com', 'test_password')

    def test_view_with_user_authenticated(self):
        test_user = self.create_test_user()
        self.client.login(username=test_user.username, password='test_password')
        response = self.client.get(self.user_profile_detail_url)
        request_context = response.context
        self.assertEqual(request_context['user'], test_user,
            'Expected request context user to be equal to request context user')
