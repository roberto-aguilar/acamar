from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from common import validators


class TestAuthenticationValidators(TestCase):

    def create_inactive_user(self):
        test_user = User.objects.create_user('test_username', 'test@test.com', 'test_password')
        test_user.is_active = False
        test_user.save()
        return test_user

    def test_validate_user_exists_with_user_that_does_not_exist_(self):
        expected_exception_message = 'The "{username}" account does not exists'.format(username='test_username')
        self.assertRaisesMessage(ValidationError, expected_exception_message,
            validators.validate_user_exists, ('test_username'))

    def test_validate_user_is_active_with_inactive_user(self):
        test_user = self.create_inactive_user()
        expected_exception_message = 'The account with username "{username}" is inactive'.format(
            username=test_user.username)
        self.assertRaisesMessage(ValidationError, expected_exception_message,
                validators.validate_user_is_active, (test_user.username))
