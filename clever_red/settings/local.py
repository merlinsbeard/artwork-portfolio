from .base import *
import environ
REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAdminUser',
            ],
        'PAGE_SIZE': 10
        }

EMAIL_USE_TLS=True

#EMAIL_HOST=os.environ['EMAIL_HOST']
#EMAIL_PORT=os.environ['EMAIL_PORT']
#EMAIL_HOST_USER=os.environ['EMAIL_HOST_USER']
#EMAIL_HOST_PASSWORD=os.environ['EMAIL_HOST_PASSWORD']

root = environ.Path(__file__) - 3
env = environ.Env()
environ.Env.read_env(root.path('.localenv')())

GRAPE = env.email()
DEBUG = env('DEBUG')
SECRET_KEY=env('SECRET_KEY')

email_settings = env.email()

EMAIL_HOST_PASSWORD=email_settings['EMAIL_HOST_PASSWORD']
EMAIL_HOST=email_settings['EMAIL_HOST']
EMAIL_PORT=email_settings['EMAIL_PORT']
EMAIL_HOST_USER=email_settings['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD=email_settings['EMAIL_HOST_PASSWORD']

# DATABASE CONFIG
DATABASES = {
    'default': env.db(),
    
}
# STATIC and MEDIA settings
STATIC_URL=env('STATIC_URL')
STATIC_ROOT=env('STATIC_ROOT')
MEDIA_URL=env('MEDIA_URL')
MEDIA_ROOT=env('MEDIA_ROOT')
