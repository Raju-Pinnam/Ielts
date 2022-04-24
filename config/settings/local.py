from .base import *

print("Using Local Settings")

DEBUG = True
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'ielts_db',
#         'USER': 'postgres',
#         'PASSWORD': 'raju@123',
#         'HOST': 'localhost',
#         'PORT': '5432',
#         'LIVE_TEST_DB': True
#     }
# }