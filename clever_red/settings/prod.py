from .base import *
import environ

root = environ.Path(__file__) - 3
env = environ.Env()
environ.Env.read_env(root.path('config/prod.env')())

#DEBUG = env('DEBUG')
DEBUG = False

EMAIL_USE_TLS=True

SECRET_KEY=env('SECRET_KEY')

email_settings = env.email()

EMAIL_HOST_PASSWORD=email_settings['EMAIL_HOST_PASSWORD']
EMAIL_HOST=email_settings['EMAIL_HOST']
EMAIL_PORT=email_settings['EMAIL_PORT']
EMAIL_HOST_USER=email_settings['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD=email_settings['EMAIL_HOST_PASSWORD']
EMAIL_TO=env('EMAIL_TO')

# DATABASE CONFIG

DATABASES = {
    'default': env.db(),
}

# STATIC and MEDIA settings
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = os.getenv('GS_BUCKET_NAME', 'benray-artwork')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django': {
            'level': 'ERROR',
            'handlers': ['console'],
        },
        '': {
            'level': 'DEBUG',
            'handlers': ['console']
        }
    }
}
