from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from accounts import models, forms


class TestUserProfileCreateView(TestCase):

    def setUp(self):
        self.create_user_profile_url = reverse('accounts:create_user_profile')

    def create_test_user_profile(self):
        test_user = User.objects.create_user(
            username='test_username', email='test@test.com',
            password='test_password'
            )
        return models.UserProfile.objects.create(
            authentication_user=test_user
            )

    def test_view_with_user_not_authenticated(self):
        response = self.client.get(self.create_user_profile_url)
        self.assertTemplateUsed(
            response=response,
            template_name='accounts/create_user_profile.html'
            )
        form = response.context['form']
        self.assertEqual(
            form.__class__, forms.UserProfileCreateForm,
            'Expected form class to be UserProfileCreateForm'
            )

    def test_view_with_user_authenticated(self):
        detail_user_profile_url = reverse('accounts:detail_user_profile')
        self.create_test_user_profile()
        self.client.login(username='test_username', password='test_password')
        response = self.client.get(self.create_user_profile_url)
        self.assertRedirects(
            response=response, expected_url=detail_user_profile_url
            )

    def test_view_with_invalid_data_provided(self):
        form_data = {
            'username': '',
            'password': '',
            'confirm_password': '',
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        response = self.client.post(self.create_user_profile_url, form_data)
        form = response.context['form']
        self.assertFalse(
            form.is_valid(),
            'Expected form to be invalid without required fields provided'
            )
        self.assertIn(
            'first_name', form.errors,
            'Expected "first_name" to be in form errors'
            )
        self.assertIn(
            'last_name', form.errors,
            'Expected "last_name" to be in form errors'
            )
        self.assertIn(
            'email', form.errors,
            'Expected "email" to be in form errors'
            )
        messages_storage = response.context['messages']
        loaded_messages = [
            message.message for message in messages_storage._loaded_messages
            ]
        self.assertIn(
            'There was an error trying to create user profile', loaded_messages,
            'Expected error message to be in loaded messages'
            )

    def test_view_with_valid_data_provided(self):
        login_url = reverse('accounts:login')
        form_data = {
            'username': 'test_username',
            'password': 'test_password',
            'confirm_password': 'test_password',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test@test.com'
        }
        response = self.client.post(
            self.create_user_profile_url, form_data, follow=True
            )
        self.assertRedirects(
            response=response, expected_url=login_url
            )
        messages_storage = response.context['messages']
        loaded_messages = [
            message.message for message in messages_storage._loaded_messages
            ]
        self.assertIn(
            'User profile created successfully', loaded_messages,
            'Expected error message to be in loaded messages'
            )
