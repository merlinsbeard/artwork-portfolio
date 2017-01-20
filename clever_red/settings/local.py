from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'local.sqlite3'),
        'NAME': BASE_DIR.child('local_db.sqlite3')
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
