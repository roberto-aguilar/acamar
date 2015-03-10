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
    filename = "{file_name}.{file_extension}".format(file_name=uuid.uuid4(), file_extension=file_extension)
    path = os.path.join('accounts/user_profile', filename)
    return path


class UserProfile(models.Model):
    authentication_user = models.OneToOneField(User)
    image = models.ImageField(upload_to=get_file_path, default='{url}{image_path}'.format(
        url=settings.STATIC_URL, image_path='accounts/img/profile-photo.png'), blank=True)

    def __unicode__(self):
        user_full_name = self.authentication_user.get_full_name()
        email = self.authentication_user.email
        return '{user_full_name} - {email}'.format(user_full_name=user_full_name, email=email)
