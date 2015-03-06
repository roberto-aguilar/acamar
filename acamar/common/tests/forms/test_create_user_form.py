from django.test import TestCase
from django.contrib.auth.models import User
from common import forms


class TestRegisterForm(TestCase):

    def test_form_with_mismatchs_passwords_provided(self):
        form_data = {
            'password': 'password',
            'confirm_password': 'mismatched_password'
        }
        form = forms.CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid(),
            'Expected form invalid with mismatched passwords provided')
        self.assertIn('password', form.errors,
            'Expected password form field to be in form errors')
        self.assertIn('confirm_password', form.errors,
            'Expected confirm password form field to be in form errors')

    def test_form_without_required_fields_provided(self):
        form_data = {
            'username': 'test_username',
            'password': 'test_password',
            'confirm_password': 'test_password',
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        form = forms.CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid(),
            'Expected form invalid without required fields provided')
        self.assertIn('first_name', form.errors,
            'Expected first_name form field to be in form errors')
        self.assertIn('last_name', form.errors,
            'Expected last_name form field to be in form errors')
        self.assertIn('email', form.errors,
            'Expected email form field to be in form errors')

    def test_form_with_correct_data(self):
        form_data = {
            'username': 'test_username',
            'password': 'test_password',
            'confirm_password': 'test_password',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test@test.com'
        }
        form = forms.CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid(),
            'Expected form to be valid with correct data provided')
        form.save()
        user = User.objects.get(username=form_data['username'])
        self.assertTrue(user.check_password(form_data['password']),
            'Expected user saved password to be equal to form data provided password')
