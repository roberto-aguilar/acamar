from django.test import TestCase
from django.core.urlresolvers import reverse


class TestRegisterView(TestCase):

    def setUp(self):
        self.register_url = reverse('common:register')

    def test_register_view_with_correct_data_provided(self):
        success_url = reverse('common:login')
        form_data = {
            'username': 'test_username',
            'password': 'test_password',
            'confirm_password': 'test_password',
            'first_name': 'test_name',
            'last_name': 'test_last_name',
            'email': 'test@test.com'
        }
        response = self.client.post(self.register_url, form_data)
        self.assertRedirects(response, expected_url=success_url,
            msg_prefix='Expected redirect after correct data provided')
