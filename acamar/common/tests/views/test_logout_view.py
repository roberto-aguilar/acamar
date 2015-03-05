from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class TestLogoutView(TestCase):

    def setUp(self):
        self.logout_url = reverse('common:logout')

    def test_logout_view_with_user_not_authenticated(self):
        index_url = reverse('common:index')
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, expected_url=index_url,
            msg_prefix='Expected response redirect to index view with user not authenticated')

    def test_logout_view_with_user_authenticated(self):
        index_url = reverse('common:index')
        User.objects.create_user('test_username', 'test@test.com', 'test_password')
        self.client.login(username='test_username', password='test_password')
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, expected_url=index_url,
            msg_prefix='Expected response redirect to index view with user not authenticated')
        """
        Given that test client response is not a real HttpResponse, the is_authenticated() method is achieved
        looking for the key '_auth_user_id' in the test client session dictionary. If is not, then the user is
        not authenticated anymore.
        """
        self.assertNotIn('_auth_user_id', self.client.session,
            'Expected user not to be authenticated')
