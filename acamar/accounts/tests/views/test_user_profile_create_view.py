from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from accounts import models, forms


class TestUserProfileCreateView(TestCase):

    def setUp(self):
        self.create_user_profile_url = reverse('accounts:create_user_profile')

    def create_test_user_profile(self):
        test_user = User.objects.create_user(
            username='test_username', email='test@test.com',
            password='test_password')
        return models.UserProfile.objects.create(
            authentication_user=test_user)

    def test_view_with_user_not_authenticated(self):
        response = self.client.get(self.create_user_profile_url)
        self.assertTemplateUsed(
            response=response,
            template_name='accounts/create_user_profile.html')
        form = response.context['form']
        self.assertEqual(form.__class__, forms.UserProfileCreateForm,
            'Expected view form class to be UserProfileCreateForm')

    def test_view_with_user_authenticated(self):
        self.create_test_user_profile()
        detail_user_profile_url = reverse('accounts:detail_user_profile')
        self.client.login(username='test_username', password='test_password')
        response = self.client.get(self.create_user_profile_url)
        self.assertRedirects(response, expected_url=detail_user_profile_url)

    def test_view_with_correct_data_provided(self):
        success_url = reverse('accounts:login')
        base64_image = b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00'  # noqa
        form_data = {
            'username': 'test_username_view',
            'password': 'test_password',
            'confirm_password': 'test_password',
            'first_name': 'test_name',
            'last_name': 'test_last_name',
            'email': 'test@test.com',
            'image': SimpleUploadedFile(content=base64_image,
                name='profile-photo.png', content_type='image/jpeg')
        }
        response = self.client.post(self.create_user_profile_url, form_data, follow=True)
        self.assertRedirects(response, expected_url=success_url,
            msg_prefix='Expected redirect after correct data provided')
        messages_storage = response.context['messages']
        loaded_messages = [message.message for message in messages_storage._loaded_messages]
        self.assertIn('User profile created successfully', loaded_messages,
            'Expected message to be in loaded messages')

    def test_view_without_required_fields_in_data_provided(self):
        base64_image = b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00'  # noqa
        form_data = {
            'username': 'test_username_view',
            'password': 'test_password',
            'confirm_password': 'test_password',
            'first_name': '',
            'last_name': '',
            'email': '',
            'image': SimpleUploadedFile(content=base64_image,
                name='profile-photo.png', content_type='image/jpeg')
        }
        response = self.client.post(self.create_user_profile_url, form_data)
        messages_storage = response.context['messages']
        loaded_messages = [message.message for message in messages_storage._loaded_messages]
        self.assertIn('There was an error trying to create user profile', loaded_messages,
            'Expected message to be in loaded messages')
        form = response.context['form']
        self.assertIn('first_name', form.errors,
            'Expected first name form field to be in form errors')
        self.assertIn('last_name', form.errors,
            'Expected last name form field to be in form errors')
        self.assertIn('email', form.errors,
            'Expected email form field to be in form errors')

    def test_view_with_mismatch_passwords_provided(self):
        base64_image = b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00'  # noqa
        form_data = {
            'username': 'test_username_view',
            'password': 'test_password',
            'confirm_password': 'invalid_password',
            'first_name': 'test_name',
            'last_name': 'test_last_name',
            'email': 'test@test.com',
            'image': SimpleUploadedFile(content=base64_image,
                name='profile-photo.png', content_type='image/jpeg')
        }
        response = self.client.post(self.create_user_profile_url, form_data)
        messages_storage = response.context['messages']
        loaded_messages = [message.message for message in messages_storage._loaded_messages]
        self.assertIn('There was an error trying to create user profile', loaded_messages,
            'Expected message to be in loaded messages')
        form = response.context['form']
        self.assertIn('password', form.errors,
            'Expected password form field to be in form errors')
        self.assertIn('confirm_password', form.errors,
            'Expected confirm password form field to be in form errors')
