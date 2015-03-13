from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from accounts import models, forms


class TestLoginView(TestCase):

    def setUp(self):
        self.login_url = reverse('accounts:login')

    def create_test_user_profile(self):
        test_user = User.objects.create_user(
            username='test_username', email='test@test.com',
            password='test_password')
        return models.UserProfile.objects.create(
            authentication_user=test_user)

    def test_view_with_user_authenticated(self):
        user_profile_detail_url = reverse('accounts:detail_user_profile')
        self.create_test_user_profile()
        self.client.login(username='test_username', password='test_password')
        response = self.client.get(self.login_url, follow=True)
        self.assertRedirects(
            response=response, expected_url=user_profile_detail_url)
        messages_storage = response.context['messages']
        loaded_messages = [message.message for message in messages_storage._loaded_messages]
        self.assertIn('Already logged in', loaded_messages,
            'Expect message to be in loaded messages')

    def test_view_with_user_not_authenticated(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(
            response=response, template_name='accounts/login.html')
        form = response.context['form']
        self.assertEqual(form.__class__, forms.AuthenticationForm,
            'Expected form class to be AuthenticationForm')
        self.assertIn('next_url', form.initial,
            'Expected next_url form field to be in form initial data')

    def test_view_with_user_not_authenticated_and_with_next_url_parameter(self):
        detail_user_profile_url = reverse('accounts:detail_user_profile')
        response = self.client.get(self.login_url, {
            'next': detail_user_profile_url
        })
        self.assertTemplateUsed(
            response=response, template_name='accounts/login.html')
        form = response.context['form']
        self.assertEqual(form.__class__, forms.AuthenticationForm,
            'Expected form class to be AuthenticationForm')
        self.assertIn('next_url', form.initial,
            'Expected next_url form field to be in form initial data')
        self.assertEqual(detail_user_profile_url, form.initial['next_url'],
            'Expected user profile url to be equal to form initial next_url')

    def test_view_with_user_not_authenticated_and_valid_authentication_data_provided(self):
        self.create_test_user_profile()
        user_profile_detail_url = reverse('accounts:detail_user_profile')
        form_data = {
            'username': 'test_username',
            'password': 'test_password'
        }
        response = self.client.post(self.login_url, form_data, follow=True)
        self.assertRedirects(response, expected_url=user_profile_detail_url)
        messages_storage = response.context['messages']
        loaded_messages = [message.message for message in messages_storage._loaded_messages]
        self.assertIn('Successful login', loaded_messages,
            'Expect message to be in loaded messages')

    def test_view_with_user_not_authenticated_and_valid_authentication_data_provided_including_next_url_parameter(self):
        self.create_test_user_profile()
        user_profile_detail_url = reverse('accounts:detail_user_profile')
        form_data = {
            'username': 'test_username',
            'password': 'test_password',
            'next_url': user_profile_detail_url
        }
        response = self.client.post(self.login_url, form_data, follow=True)
        self.assertRedirects(response, expected_url=user_profile_detail_url)
        messages_storage = response.context['messages']
        loaded_messages = [message.message for message in messages_storage._loaded_messages]
        self.assertIn('Successful login', loaded_messages,
            'Expect message to be in loaded messages')

    def test_view_with_user_not_authenticated_and_invalid_authentication_data_provided(self):
        self.create_test_user_profile()
        form_data = {
            'username': 'test_username',
            'password': 'incorrect_password'
        }
        response = self.client.post(self.login_url, form_data)
        form = response.context['form']
        self.assertFalse(form.is_valid(),
            'Expect form to be invalid with incorrect data provided')
        self.assertIn('password', form.errors,
            'Expected password form field to be in form errors')
        messages_storage = response.context['messages']
        loaded_messages = [message.message for message in messages_storage._loaded_messages]
        self.assertIn('There was an error trying login', loaded_messages,
            'Expect message to be in loaded messages')
