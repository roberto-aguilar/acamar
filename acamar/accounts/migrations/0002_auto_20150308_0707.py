# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models.user_profile


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default=b'/static//accounts/img/profile-photo.png', upload_to=accounts.models.user_profile.get_file_path),
            preserve_default=True,
        ),
    ]
