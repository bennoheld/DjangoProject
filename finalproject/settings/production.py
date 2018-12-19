# Load defaults in order to then add/override with production-only settings
from .defaults import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'options': '-c search_path=studentmanager_grimmeisen_scholtz'
        },
        'NAME': 'Datenbank WIC',
        'USER': 'WICWS1813',
        'PASSWORD': get_env_variable('STUDENTMANAGER_POSTGRESQL_PASS'),
        'HOST': '193.93.243.162',
        'PORT': '5432'
    },
}
