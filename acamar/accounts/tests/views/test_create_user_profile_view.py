from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


class TestCreateUserProfileView(TestCase):

    def setUp(self):
        self.register_url = reverse('accounts:register')

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
        response = self.client.post(self.register_url, form_data, follow=True)
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
        response = self.client.post(self.register_url, form_data)
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
        response = self.client.post(self.register_url, form_data)
        messages_storage = response.context['messages']
        loaded_messages = [message.message for message in messages_storage._loaded_messages]
        self.assertIn('There was an error trying to create user profile', loaded_messages,
            'Expected message to be in loaded messages')
        form = response.context['form']
        self.assertIn('password', form.errors,
            'Expected password form field to be in form errors')
        self.assertIn('confirm_password', form.errors,
            'Expected confirm password form field to be in form errors')
