from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('Jacob Guzman', 'jgacosta@dojogeek.io '),
    ('Roberto Aguilar', 'raguilar@dojogeek.io '),
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'kI2ZJsv3Yi',
        'HOST': 'localhost',
        'PORT': '',
        'CONN_MAX_AGE': 600,
    }
}

ALLOWED_HOSTS = ['104.131.49.161']

TEMPLATE_DEBUG = False
