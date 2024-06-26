
from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-03n6+4xlmi$iw65a6228zu^pznk2@p5=bk2xl+9xdz4$%9e1m_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


#sites framework
SITE_ID = 2

# INSTALLED_APPS = []



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


STATICFILES_DIRS = [
    BASE_DIR / "statics",
]






CSRF_COOKIE_SECURE = False
