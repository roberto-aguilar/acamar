from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from accounts import models, validators


class TestUserProfileValidators(TestCase):

    def test_validate_username_does_not_exist_with_username_that_already_exist(self):
        test_user = User.objects.create_user('test_username', 'test@test.com', 'test_password')
        models.UserProfile.objects.create(authentication_user=test_user)
        with self.assertRaises(ValidationError) as context_manager:
            validators.validate_username_does_not_exist('test_username')
        exception = context_manager.exception
        self.assertEquals(exception.code, 'user_already_exists')
