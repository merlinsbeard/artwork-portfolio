from .base import *



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ['WORK_DATABASE'],

    }
}


DEBUG = False
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

EMAIL_USE_TLS=True

EMAIL_HOST=os.environ['EMAIL_HOST']
EMAIL_PORT=os.environ['EMAIL_PORT']
EMAIL_HOST_USER=os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD=os.environ['EMAIL_HOST_PASSWORD']
SECRET_KEY=os.environ['SECRET_KEY']
