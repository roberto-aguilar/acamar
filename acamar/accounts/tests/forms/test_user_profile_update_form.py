from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from accounts import models, forms


class TestUserProfileUpdateForm(TestCase):

    def create_test_user_profile(self):
        kwargs = {
            'username': 'test_username',
            'email': 'test@test.com',
            'password': 'test_password',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name'
        }
        test_user = User.objects.create_user(**kwargs)
        return models.UserProfile.objects.create(
            authentication_user=test_user)

    def test_form_with_valid_data_provided(self):
        test_user_profile = self.create_test_user_profile()
        form_data = {
            'first_name': 'updated_first_name',
            'last_name': 'updated_last_name',
            'email': 'updated@test.com',
        }
        form = forms.UserProfileUpdateForm(
            data=form_data,
            instance=test_user_profile.authentication_user)
        self.assertTrue(
            form.is_valid(),
            'Expected form to be valid with valid data provided')
        self.assertEqual(
            form_data['first_name'], form.cleaned_data['first_name'],
            'Expected first name provided to be equal to "first_name" form cleaned data')
        self.assertEqual(
            form_data['last_name'], form.cleaned_data['last_name'],
            'Expected last name provided to be equal to "last_name" form cleaned data')
        self.assertEqual(
            form_data['email'], form.cleaned_data['email'],
            'Expected email provided to be equal to "email" form cleaned data')
        test_user_updated = form.save()
        self.assertEqual(
            form_data['first_name'], test_user_updated.first_name,
            'Expected "first_name" provided to be equal to "user" saved "first_name"')
        self.assertEqual(
            form_data['last_name'], test_user_updated.last_name,
            'Expected "last_name" provided to be equal to "user" saved "last_name"')
        self.assertEqual(
            form_data['email'], test_user_updated.email,
            'Expected "email" provided to be equal to "user" saved "email"')

    def test_form_without_required_fields_provided(self):
        test_user_profile = self.create_test_user_profile()
        form_data = {
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        form = forms.UserProfileUpdateForm(
            form_data, instance=test_user_profile.authentication_user)
        self.assertFalse(
            form.is_valid(),
            'Expected form to be invalid without required fields provided')
        self.assertIn(
            'first_name', form.errors,
            'Expected "first_name" form field to be in form errors')
        self.assertIn(
            'last_name', form.errors,
            'Expected "last_name" form field to be in form errors')
        self.assertIn(
            'email', form.errors,
            'Expected "email" form field to be in form errors')

    def test_form_with_user_instance_that_is_not_related_to_user_profile_instance(self):
        test_user = User.objects.create_user(
            username='test_username', email='test@test.com',
            password='test_password')
        form_data = dict()
        expected_exception_message = \
            'The username "{username}" does not have a related UserProfile'.format(
                username=test_user.username)
        self.assertRaisesMessage(
            ValidationError, expected_exception_message,
            forms.UserProfileUpdateForm, **{
                'data': form_data,
                'instance': test_user
            })

    def test_form_has_image_in_initial_form_values(self):
        test_user_profile = self.create_test_user_profile()
        form = forms.UserProfileUpdateForm(
            instance=test_user_profile.authentication_user)
        self.assertIn(
            'image', form.initial,
            'Expected image form field to be in initial form values')

    def test_form_model(self):
        form = forms.UserProfileUpdateForm
        self.assertEqual(
            form._meta.model, User,
            'Expected form model to be django.contrib.auth.models.User')

    def test_form_fields(self):
        form_fields = ['first_name', 'last_name', 'email', 'image']
        test_user_profile = self.create_test_user_profile()
        form = forms.UserProfileUpdateForm(
            instance=test_user_profile.authentication_user)
        self.assertEqual(
            form_fields, form._meta.fields,
            'Expect expected form fields to be equal to form fields')
