# -*- coding: utf8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from common import forms


class TestAuthForm(TestCase):

    def test_form_is_valid_without_data(self):
        form_data = {}
        form = forms.AuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid(),
            'Form expected to be invalid without data provided')

    def test_form_is_valid_with_correct_data(self):
        User.objects.create_user('test_username', 'test@test.com', 'test_password')
        form_data = {
            'username': 'test_username',
            'password': 'test_password'
        }
        form = forms.AuthenticationForm(data=form_data)
        self.assertTrue(form.is_valid(),
            'Form expected to ve valid with correct data provided')

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
        self.assertEqual(form.errors['username'],
            ['La cuenta asociada al usuario "test_username" se encuentra desactivada'],
            'Username inactive form field error expected')

    def test_form_is_valid_with_user_that_does_not_exist(self):
        form_data = {
            'username': 'test_username',
            'password': 'test_password'
        }
        form = forms.AuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid(),
            'Form expected to be invalid with username that does not exists provided')
        self.assertEqual(form.errors['username'],
            ['No se encontro una cuenta asociada al usuario "test_username"'],
            'Username not found form field error expected')

    def test_form_is_valid_with_incorrect_password(self):
        User.objects.create_user('test_username', 'test@test.com', 'test_password')
        form_data = {
            'username': 'test_username',
            'password': 'invalid_password'
        }
        form = forms.AuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid(),
            'Form expected to be invalid with incorrect password provided')
        self.assertEqual(form.errors['password'],
            [u'Contraseña incorrecta'],
            'Password incorrect form field error expected')

    def test_form_get_user(self):
        test_user = User.objects.create_user('test_username', 'test@test.com', 'test_password')
        form_data = {
            'username': 'test_username',
            'password': 'test_password'
        }
        form = forms.AuthenticationForm(data=form_data)
        self.assertTrue(form.is_valid(),
            'Form expected to be valid with correct data provided')
        self.assertEqual(form.get_user(), test_user,
            'Form returned user expected to be equal to user provided')

    def test_form_get_user_with_user_that_does_not_exist(self):
        form_data = {
            'username': 'test_username',
            'password': 'test_password'
        }
        form = forms.AuthenticationForm(data=form_data)
        self.assertFalse(form.is_valid(),
            'Form expected to be invalid with username that does not exists provided')
        self.assertIsNone(form.get_user(),
            'None expected to be returned on invalid form')
