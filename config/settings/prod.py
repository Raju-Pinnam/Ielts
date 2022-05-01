from .base import *

print("Using Prod Settings")

DEBUG = False
ALLOWED_HOSTS = ['.heroku.com',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ielts_db',
        'USER': 'postgres',
        'PASSWORD': 'raju@123',
        'HOST': 'localhost',
        'PORT': '5432',
        'LIVE_TEST_DB': True
    }
}
