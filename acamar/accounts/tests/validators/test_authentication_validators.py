from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from accounts import validators


class TestAuthenticationValidators(TestCase):

    def create_inactive_user(self):
        test_user = User.objects.create_user(
            username='test_username', email='test@test.com',
            password='test_password')
        test_user.is_active = False
        test_user.save()
        return test_user

    def test_validate_user_exists_with_user_that_does_not_exist_(self):
        expected_exception_message = 'The "{username}" account does not exists'.format(
            username='test_username')
        self.assertRaisesMessage(ValidationError, expected_exception_message,
            validators.validate_user_exists, ('test_username'))

    def test_validate_user_is_active_with_inactive_user(self):
        test_user = self.create_inactive_user()
        expected_exception_message = 'The account with username "{username}" is inactive'.format(
            username=test_user.username)
        self.assertRaisesMessage(ValidationError, expected_exception_message,
                validators.validate_user_is_active, (test_user.username))

    def test_validate_user_is_active_with_user_that_does_not_exist(self):
        self.assertIsNone(validators.validate_user_is_active('test_username'),
            'Expected None as a return value with active username provided')
