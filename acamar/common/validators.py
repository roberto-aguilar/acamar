from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_user_exists(username):
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        raise ValidationError(
            'No se encontro una cuenta asociada al usuario "%(username)s"',
            code='user_not_found',
            params={
                'username': username
            }
        )


def validate_user_is_active(username):
    try:
        user = User.objects.get(username=username)
        if user.is_active is False:
            raise ValidationError(
                'La cuenta asociada al usuario "%(username)s" se encuentra desactivada',
                code='user_not_active',
                params={
                    'username': username
                }
            )
    except User.DoesNotExist:
        pass  # Already validated in validate_user_exists(username)
