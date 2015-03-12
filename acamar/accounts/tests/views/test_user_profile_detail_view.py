from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class TestUserProfileDetailView(TestCase):

    def setUp(self):
        self.user_profile_detail_url = reverse('accounts:detail_user_profile')

    def test_view_with_user_authenticated(self):
        test_user = User.objects.create_user('test_username', 'test@test.com', 'test_password')
        self.client.login(username='test_username', password='test_password')
        response = self.client.get(self.user_profile_detail_url)
        request_context = response.context
        self.assertEqual(request_context['user'], test_user,
            'Expected request context user to be equal to request context user')

    def test_view_with_user_not_authenticated(self):
        response = self.client.get(self.user_profile_detail_url)
        login_url = reverse('accounts:login')
        expected_url = '{login_url}?next={source_url}'.format(
            login_url=login_url, source_url=self.user_profile_detail_url)
        self.assertRedirects(response, expected_url=expected_url,
            msg_prefix='Expected response redirect to user login view on users not authenticated')
