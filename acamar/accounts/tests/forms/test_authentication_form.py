from django.test import TestCase
from django.contrib.auth.models import User
from accounts import forms, validators


class TestAuthenticationForm(TestCase):

    def create_test_user(self):
        return User.objects.create_user(
            username='test_username', email='test@test.com',
            password='test_password'
            )

    def test_validators_in_username_field(self):
        form = forms.AuthenticationForm
        form_validators = form.base_fields['username'].validators
        self.assertIn(
            validators.validate_user_exists, form_validators,
            'Expected validate_user_exists to be in form username validators'
            )
        self.assertIn(
            validators.validate_user_is_active, form_validators,
            'Expected validate_user_is_active to be in form username validators'
            )

    def test_form_is_valid_with_correct_data_provided(self):
        self.create_test_user()
        form_data = {
            'username': 'test_username',
            'password': 'test_password'
        }
        form = forms.AuthenticationForm(data=form_data)
        self.assertTrue(
            form.is_valid(),
            'Form expected to ve valid with correct data provided'
            )
        self.assertIn(
            'user_authenticated', form.cleaned_data,
            'Expected user authenticated to be in form cleaned data'
            )

    def test_form_is_invalid_with_incorrect_password(self):
        self.create_test_user()
        form_data = {
            'username': 'test_username',
            'password': 'invalid_password'
        }
        form = forms.AuthenticationForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            'Form expected to be invalid with incorrect password provided'
            )
        self.assertIn(
            'password', form.errors,
            'Expected password form field to be in form errors'
            )
        self.assertNotIn(
            'username', form.errors,
            'Expected username not to be in form field errors'
            )
        self.assertNotIn(
            'next_url', form.errors,
            'Expected next_url not to be in form field errors'
            )
