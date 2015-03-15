from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from accounts import models, validators


class TestUserProfileValidators(TestCase):

    def test_username_does_not_exist_with_username_that_already_exist(self):
        test_user = User.objects.create_user(
            username='test_username', email='test@test.com',
            password='test_password')
        models.UserProfile.objects.create(authentication_user=test_user)
        expected_exception_message = \
            'The username "{username}" already exists'.format(
                username=test_user.username)
        self.assertRaisesMessage(
            ValidationError, expected_exception_message,
            validators.validate_username_does_not_exist, test_user.username)
