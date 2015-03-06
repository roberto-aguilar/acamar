from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


def validate_username_does_not_exist(username):
    try:
        if User.objects.get(username=username):
            raise ValidationError(
                _('The username "%(username)s" already exists'),
                code='user_already_exist',
                params={
                    'username': username
                })
    except User.DoesNotExist:
        pass  # Username available
