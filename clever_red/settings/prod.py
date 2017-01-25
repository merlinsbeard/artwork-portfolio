from .base import *



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ['WORK_DATABASE'],

    }
}


DEBUG = True
STATIC_URL=os.environ['STATIC_URL']
STATIC_ROOT=os.environ['STATIC_ROOT']
MEDIA_URL=os.environ['MEDIA_URL']
MEDIA_ROOT=os.environ['MEDIA_ROOT']
REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAdminUser',
            ],
        'PAGE_SIZE': 10
        }
