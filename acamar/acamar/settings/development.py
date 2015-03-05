from .base import *  # noqa

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vagrant',
        'USER': 'vagrant',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'CONN_MAX_AGE': 600,
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# This ip addresses ensure debug toolbar shows development environment
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')
