from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from accounts import models


class TestIndexView(TestCase):

    def setUp(self):
        self.index_url = reverse('common:index')

    def create_test_user(self):
        test_user = User.objects.create_user(
            username='test_username', email='test@test.com',
            password='test_password'
            )
        return models.UserProfile.objects.create(
            authentication_user=test_user
            )

    def test_view_with_user_not_authenticated(self):
        response = self.client.get(self.index_url)
        self.assertTemplateUsed(
            response=response, template_name='common/index.html'
            )

    def test_view_with_user_authenticated(self):
        user_profile_detail_url = reverse('accounts:detail_user_profile')
        self.create_test_user()
        self.client.login(username='test_username', password='test_password')
        response = self.client.get(self.index_url, follow=True)
        self.assertRedirects(response, expected_url=user_profile_detail_url)
