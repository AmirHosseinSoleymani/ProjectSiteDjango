
from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-03n6+4xlmi$iw65a6228zu^pznk2@p5=bk2xl+9xdz4$%9e1m_'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['bookovie.ir','www.bookovie.ir']


#sites framework
SITE_ID = 4

# INSTALLED_APPS = []



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'bookovie_site',  
        'USER': 'bookovie_admin',  
        'PASSWORD': 'aAx7S{xpF,R~',  
        'HOST': '127.0.0.1',  
        'PORT': '3306',   
    }  
}  

STATIC_ROOT = '/home/bookovie/public_html/static'
MEDIA_ROOT = '/home/bookovie/public_html/media'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


STATICFILES_DIRS = [
    BASE_DIR / "statics",
]




CSRF_COOKIE_SECURE = False  

