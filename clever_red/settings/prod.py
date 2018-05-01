from .base import *
import environ

root = environ.Path(__file__) - 3
env = environ.Env()
environ.Env.read_env(root.path('.prodenv')())

#DEBUG = env('DEBUG')
DEBUG = False
REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAdminUser',
            ],
        'PAGE_SIZE': 10
        }

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
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'artwork'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'postgres'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# STATIC and MEDIA settings
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = os.getenv('GS_BUCKET_NAME', 'benray-artwork')
