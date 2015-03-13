from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from accounts import models


class TestUserProfileDetailView(TestCase):

    def setUp(self):
        self.user_profile_detail_url = reverse('accounts:detail_user_profile')

    def create_test_user_profile(self):
        test_user = User.objects.create_user(
            username='test_username', email='test@test.com',
            password='test_password')
        return models.UserProfile.objects.create(
            authentication_user=test_user)

    def test_view_with_user_not_authenticated(self):
        login_url = reverse('accounts:login')
        expected_url = '{login_url}?next={user_profile_detail_url}'.format(
            login_url=login_url,
            user_profile_detail_url=self.user_profile_detail_url)
        response = self.client.get(self.user_profile_detail_url, follow=True)
        self.assertRedirects(response, expected_url=expected_url)

    def test_view_with_user_authenticated(self):
        test_user_profile = self.create_test_user_profile()
        self.client.login(username='test_username', password='test_password')
        response = self.client.get(self.user_profile_detail_url)
        self.assertTemplateUsed(response=response,
            template_name='accounts/detail_user_profile.html')
        self.assertIn('user_profile', response.context,
            'Expected request user profile to be in response context')
        self.assertEqual(test_user_profile, response.context['user_profile'],
            'Expected request user profile to be equal to response user profile')
