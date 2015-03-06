from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from common import validators


class TestCreateUserValidators(TestCase):

    def test_username_does_not_exist_with_user_that_exist(self):
        expected_exception_code = 'user_already_exist'
        User.objects.create_user('test_username', 'test@test.com', 'test_username')
        with self.assertRaises(ValidationError) as context_manager:
            validators.validate_username_does_not_exist('test_username')
        exception = context_manager.exception
        self.assertEqual(exception.code, expected_exception_code,
            'Expected exception code {expected_exception_code}, received instead {exception_code}'.format(
                expected_exception_code=expected_exception_code, exception_code=exception.code))
