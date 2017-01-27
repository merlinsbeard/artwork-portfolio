from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'local.sqlite3'),
        #'NAME': BASE_DIR.child('ola.sqlite3')
        'NAME': os.environ['WORK_DATABASE'],
    }
}

STATIC_URL= 'http://localhost:8080/static/'
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#    '/vagrant/html/static/'
#]
STATIC_ROOT = '/vagrant/html/static/'
STATIC_ROOT = BASE_DIR.child('static')

# During Development only
MEDIA_URL = 'http://localhost:8080/static/media/'
MEDIA_ROOT = '/vagrant/html/static/media/'
MEDIA_ROOT = BASE_DIR.child('static') + 'media/'
#MEDIA_ROOT = os.path.join(BASE_DIR,'/media/')
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

EMAIL_USE_TLS=True

EMAIL_HOST=os.environ['EMAIL_HOST']
EMAIL_PORT=os.environ['EMAIL_PORT']
EMAIL_HOST_USER=os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD=os.environ['EMAIL_HOST_PASSWORD']
SECRET_KEY=os.environ['SECRET_KEY']
