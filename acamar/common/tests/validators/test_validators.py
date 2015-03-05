from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from common.validators import authentication_validators


class TestValidators(TestCase):

    def test_validate_user_exists_with_user_that_doesnt_exist(self):
        self.assertRaises(ValidationError, authentication_validators.validate_user_exists, 'test_username')

    def test_validate_user_exists_with_existing_user(self):
        User.objects.create_user('test_username', 'test@test.com', 'test_password')
        self.assertIsNone(authentication_validators.validate_user_exists('test_username'),
            'Expected that validator returns None on succesfull validation')

    def test_validate_user_is_active_with_inactive_user(self):
        test_user = User.objects.create_user('test_username', 'test@test.com', 'test_password')
        test_user.is_active = False
        test_user.save()
        self.assertRaises(ValidationError, authentication_validators.validate_user_is_active, 'test_username')

    def test_validate_user_is_active_with_active_user(self):
        User.objects.create_user('test_username', 'test@test.com', 'test_password')
        self.assertIsNone(authentication_validators.validate_user_is_active('username'),
            'Expected that validator returns None no succesfull validation')
