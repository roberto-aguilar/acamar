from django.test import TestCase
from common.forms import create_user_form


class TestRegisterForm(TestCase):

    def test_register_form_with_mismatchs_passwords_provided(self):
        form_data = {
            'password': 'password',
            'confirm_password': 'mismatched_password'
        }
        form = create_user_form.CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid(),
            'Expected form invalid with mismatched passwords provided')
        self.assertIn('password', form.errors,
            'Expected password form field to be in form errors')
        self.assertIn('confirm_password', form.errors,
            'Expected confirm password form field to be in form errors')

    def test_register_form_without_required_fields_provided(self):
        form_data = {
            'username': 'test_username',
            'password': 'test_password',
            'confirm_password': 'test_password',
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        form = create_user_form.CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid(),
            'Expected form invalid without required fields provided')
        self.assertIn('first_name', form.errors,
            'Expected first_name form field to be in form errors')
        self.assertIn('last_name', form.errors,
            'Expected last_name form field to be in form errors')
        self.assertIn('email', form.errors,
            'Expected email form field to be in form errors')
