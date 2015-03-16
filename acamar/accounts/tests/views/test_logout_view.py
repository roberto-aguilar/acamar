from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY


class TestLogoutView(TestCase):

    def setUp(self):
        self.logout_url = reverse('accounts:logout')

    def test_logout_view_with_user_not_authenticated(self):
        index_url = reverse('common:index')
        response = self.client.get(self.logout_url, follow=True)
        self.assertRedirects(response, expected_url=index_url)
        messages_storage = response.context['messages']
        loaded_messages = [
            message.message for message in messages_storage._loaded_messages
            ]
        self.assertIn(
            'There is no user logged in', loaded_messages,
            'Expected message to be in loaded messages'
            )

    def test_logout_view_with_user_authenticated(self):
        index_url = reverse('common:index')
        User.objects.create_user(
            username='test_username', email='test@test.com',
            password='test_password'
            )
        self.client.login(username='test_username', password='test_password')
        response = self.client.get(self.logout_url, follow=True)
        self.assertRedirects(response, expected_url=index_url)
        """
        Given that test client response is not a real HttpResponse,
        the is_authenticated() method is achieved looking for the SESSION_KEY
        in the test client session dictionary. If is not, then the user is not
        authenticated.
        """
        self.assertNotIn(
            SESSION_KEY, self.client.session,
            'Expected user not to be authenticated')
        messages_storage = response.context['messages']
        loaded_messages = [
            message.message for message in messages_storage._loaded_messages
            ]
        self.assertIn(
            'Logout successful', loaded_messages,
            'Expected message to be in loaded messages'
            )
