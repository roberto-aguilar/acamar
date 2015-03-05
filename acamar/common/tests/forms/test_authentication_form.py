from django.test import TestCase
from django.contrib.auth.models import User
from common import forms


class TestAuthForm(TestCase):

    def test_form_is_valid_with_correct_data(self):
        User.objects.create_user('test_username', 'test@test.com', 'test_password')
        form_data = {
            'username': 'test_username',
            'password': 'test_password'
        }
        form = forms.AuthenticationForm(data=form_data)
        self.assertTrue(form.is_valid(),
            'Form expected to ve valid with correct data provided')
        self.assertIn('user_authenticated', form.cleaned_data,
            'Expected user authenticated to be in form cleaned data')

    def test_form_is_valid_with_inactive_user(self):
        test_user = User.objects.create_user('test_username', 'test@test.com', 'test_password')
        test_user.is_active = False
        test_user.save()
        form_data = {
            'username': 'test_username',
            'password': 'test_password'
        }
        form = forms.AuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid(),
            'Form expected to be invalid with username inactive provided')
        self.assertIn('username', form.errors,
            'Expected username form field to be in form errors')
        self.assertNotIn('password', form.errors,
            'Expected password not to be in form field errors, received instead {errors}'.format(
                errors=form.errors.get('password')))

    def test_form_is_valid_with_user_that_does_not_exist(self):
        form_data = {
            'username': 'test_username',
            'password': 'test_password'
        }
        form = forms.AuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid(),
            'Form expected to be invalid with username that does not exists provided')
        self.assertIn('username', form.errors,
            'Expected username form field to be in form errors')
        self.assertNotIn('password', form.errors,
            'Expected password not to be in form field errors, received instead {errors}'.format(
                errors=form.errors.get('password')))

    def test_form_is_valid_with_incorrect_password(self):
        User.objects.create_user('test_username', 'test@test.com', 'test_password')
        form_data = {
            'username': 'test_username',
            'password': 'invalid_password'
        }
        form = forms.AuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid(),
            'Form expected to be invalid with incorrect password provided')
        self.assertIn('password', form.errors,
            'Expected password form field to be in form errors')
        self.assertNotIn('username', form.errors,
            'Expected username not to be in form field errors, received instead {errors}'.format(
                errors=form.errors.get('username')))
