from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from common import validators


class TestAuthenticationValidators(TestCase):

    def test_validate_user_exists_with_user_that_doesnt_exist(self):
        expected_exception_code = 'user_not_found'
        with self.assertRaises(ValidationError) as context_manager:
            validators.validate_user_exists('test_username')
        exception = context_manager.exception
        self.assertEqual(exception.code, expected_exception_code,
            'Expected exception code {expected_exception_code}, received instead {exception_code}'.format(
                expected_exception_code=expected_exception_code, exception_code=exception.code))

    def test_validate_user_is_active_with_inactive_user(self):
        test_user = User.objects.create_user('test_username', 'test@test.com', 'test_password')
        test_user.is_active = False
        test_user.save()
        expected_exception_code = 'user_not_active'
        with self.assertRaises(ValidationError) as context_manager:
            validators.validate_user_is_active('test_username')
        exception = context_manager.exception
        self.assertEqual(exception.code, expected_exception_code,
            'Expected exception code {expected_exception_code}, received instead {exception_code}'.format(
                expected_exception_code=expected_exception_code, exception_code=exception.code))
