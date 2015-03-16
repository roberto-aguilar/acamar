from django.test import TestCase
from django import forms as django_forms
from django.contrib.auth.models import User
from accounts.validators import validate_username_does_not_exist
from accounts import forms


class TestUserProfileCreateForm(TestCase):

    def test_form_with_correct_data_provided(self):
        form_data = {
            'username': 'test_username',
            'password': 'test_password',
            'confirm_password': 'test_password',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test@test.com'
        }
        form = forms.UserProfileCreateForm(data=form_data)
        self.assertTrue(
            form.is_valid(),
            'Expected form to be valid with correct data provided'
            )

    def test_form_without_required_fields_provided(self):
        form_data = {
            'username': 'test_username',
            'password': 'test_password',
            'confirm_password': 'test_password',
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        form = forms.UserProfileCreateForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            'Expected form invalid without required fields provided'
            )
        self.assertIn(
            'first_name', form.errors,
            'Expected first_name form field to be in form errors'
            )
        self.assertIn(
            'last_name', form.errors,
            'Expected last_name form field to be in form errors'
            )
        self.assertIn(
            'email', form.errors,
            'Expected email form field to be in form errors'
            )

    def test_form_with_mismatchs_passwords_provided(self):
        form_data = {
            'password': 'password',
            'confirm_password': 'mismatched_password'
        }
        form = forms.UserProfileCreateForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            'Expected form invalid with mismatched passwords provided'
            )
        self.assertIn(
            'password', form.errors,
            'Expected password form field to be in form errors'
            )
        self.assertIn(
            'confirm_password', form.errors,
            'Expected confirm password form field to be in form errors'
            )

    def test_form_username_has_custom_validator(self):
        form = forms.UserProfileCreateForm()
        username_validators = form.fields['username'].validators
        self.assertIn(
            validate_username_does_not_exist, username_validators,
            'Expect custom validator to be in username validators'
            )

    def test_form_model(self):
        form = forms.UserProfileCreateForm
        self.assertEqual(
            form._meta.model, User,
            'Expected form model to be django.contrib.auth.models.User'
            )

    def test_form_fields(self):
        form_fields = [
            'username', 'password', 'confirm_password', 'first_name',
            'last_name', 'email'
            ]
        form = forms.UserProfileCreateForm
        self.assertEqual(
            form._meta.fields, form_fields,
            'Expected form base fields to be equal to form fields'
            )

    def test_form_field_password_widget(self):
        form = forms.UserProfileCreateForm()
        password_widget_class = form.fields['password'].widget.__class__
        self.assertEqual(
            password_widget_class, django_forms.PasswordInput,
            'Expected password widget to be PasswordInput'
            )
