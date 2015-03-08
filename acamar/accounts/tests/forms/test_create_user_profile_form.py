from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from accounts import forms


class TestCreateUserProfileForm(TestCase):

    def test_form_with_correct_data_provided(self):
        form_data = {
            'username': 'test_username',
            'password': 'test_password',
            'confirm_password': 'test_password',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test@test.com'
        }
        base64_image = b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00'  # noqa
        form_files = {
            'image': SimpleUploadedFile(content=base64_image,
                name='profile-photo.png', content_type='image/jpeg')
        }
        form = forms.CreateUserProfileForm(data=form_data, files=form_files)
        self.assertTrue(form.is_valid(),
            'Expected form to be valid with correct data provided')

    def test_form_without_required_fields_provided(self):
        form_data = {
            'username': 'test_username',
            'password': 'test_password',
            'confirm_password': 'test_password',
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        form = forms.CreateUserProfileForm(data=form_data)
        self.assertFalse(form.is_valid(),
            'Expected form invalid without required fields provided')
        self.assertIn('first_name', form.errors,
            'Expected first_name form field to be in form errors')
        self.assertIn('last_name', form.errors,
            'Expected last_name form field to be in form errors')
        self.assertIn('email', form.errors,
            'Expected email form field to be in form errors')

    def test_form_with_mismatchs_passwords_provided(self):
        form_data = {
            'password': 'password',
            'confirm_password': 'mismatched_password'
        }
        form = forms.CreateUserProfileForm(data=form_data)
        self.assertFalse(form.is_valid(),
            'Expected form invalid with mismatched passwords provided')
        self.assertIn('password', form.errors,
            'Expected password form field to be in form errors')
        self.assertIn('confirm_password', form.errors,
            'Expected confirm password form field to be in form errors')
