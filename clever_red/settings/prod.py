from .base import *



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3')

    }
}


DEBUG = False
STATIC_URL=os.environ['STATIC_URL']
STATIC_ROOT=os.environ['STATIC_ROOT']
MEDIA_URL=os.environ['MEDIA_URL']
MEDIA_ROOT=os.environ['MEDIA_ROOT']
