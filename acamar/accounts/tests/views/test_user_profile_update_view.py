from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from accounts import models, forms


class TestUserProfileUpdateView(TestCase):

    def setUp(self):
        self.update_user_profile_url = reverse('accounts:update_user_profile')

    def create_test_user_profile(self):
        user_kwargs = {
            'username': 'test_username',
            'email': 'test@test.com',
            'password': 'test_password',
            'first_name': 'Testing',
            'last_name': 'Tester'
        }
        test_user = User.objects.create_user(**user_kwargs)
        return models.UserProfile.objects.create(
            authentication_user=test_user)

    def test_view_with_user_not_authenticated(self):
        login_url = reverse('accounts:login')
        expected_url = '{login_url}?next={current_url}'.format(
            login_url=login_url, current_url=self.update_user_profile_url)
        response = self.client.get(self.update_user_profile_url)
        self.assertRedirects(response, expected_url=expected_url)

    def test_view_with_user_authenticated(self):
        test_user_profile = self.create_test_user_profile()
        self.client.login(username='test_username', password='test_password')
        response = self.client.get(self.update_user_profile_url)
        self.assertTemplateUsed(response, 'accounts/update_user_profile.html')
        form = response.context['form']
        self.assertEqual(form.__class__, forms.UserProfileUpdateForm,
            'Expected form class to be UserProfileUpdateForm')
        self.assertEqual(form.instance, test_user_profile.authentication_user,
            'Expected form instance to be equal to request user')

    def test_view_with_valid_data_provided(self):
        self.create_test_user_profile()
        self.client.login(username='test_username', password='test_password')
        form_data = {
            'first_name': 'first_name_updated',
            'last_name': 'last_name_updated',
            'email': 'updated@test.com'
        }
        detail_user_profile_url = reverse('accounts:detail_user_profile')
        response = self.client.post(
            self.update_user_profile_url, form_data, follow=True)
        self.assertRedirects(
            response=response, expected_url=detail_user_profile_url)
        messages_storage = response.context['messages']
        loaded_messages = [message.message for message in messages_storage._loaded_messages]
        self.assertIn('User profile successfully updated', loaded_messages,
            'Expectec success message to be in loaded messages')

    def test_view_with_invalid_data_provided(self):
        self.create_test_user_profile()
        self.client.login(username='test_username', password='test_password')
        form_data = {
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        response = self.client.post(self.update_user_profile_url, form_data)
        form = response.context['form']
        self.assertFalse(form.is_valid(),
            'Expected form to be invalid without required fields provided')
        self.assertIn('first_name', form.errors,
            'Expected "first_name" to be in form errors')
        self.assertIn('last_name', form.errors,
            'Expected "last_name" to be in form errors')
        self.assertIn('email', form.errors,
            'Expected "email" to be in form errors')
        messages_storage = response.context['messages']
        loaded_messages = [message.message for message in messages_storage._loaded_messages]
        self.assertIn('An error ocurred trying to update the user profile', loaded_messages,
            'Expected error message to be in loaded messages')
