from .base import *

DEBUG = False

ALLOWED_HOSTS = []  # TODO: set domain here

SECRET_KEY = os.environ.get('MARKETPLACE_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('MARKETPLACE_DB'),
        'USER': os.environ.get('MARKETPLACE_DB_USER'),
        'PASSWORD': os.environ.get('MARKETPLACE_DB_PASSWORD'),
        'HOST': os.environ.get('MARKETPLACE_DB_HOST'),
        'PORT': os.environ.get('MARKETPLACE_DB_PORT'),
        'CONN_MAX_AGE': 120
    }
}
