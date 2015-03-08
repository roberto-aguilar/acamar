from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import uuid
import os


def get_file_path(instance, filename):
    """
    Helper function to provide user profile images an unique filename to avoid overwrites
    """
    file_extension = filename.split('.')[-1]
    filename = "{filename}.{file_extension}".format(file_name=uuid.uuid4(), file_extension=file_extension)
    path = os.path.join('accounts/user_profile', filename)
    return path


class UserProfile(models.Model):
    authentication_user = models.OneToOneField(User)
    image = models.ImageField(upload_to=get_file_path, default='{directory}/{profile_image}'.format(
        directory=settings.STATIC_ROOT, profile_image='profile-photo.png'))
