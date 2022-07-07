import os

from logging import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*6bmor_e*f$-s#fa7m5o8_!pcml8#uoyv2a8n0tc_s9(5g8m&8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bmgAPI',
    'bootstrapform'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'admApiBmg.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'admApiBmg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_HOST = "smtp.kinghost.net"
#EMAIL_HOST_USER = 'agenciaoner.send@agenciaoner.com.br'
#EMAIL_HOST_PASSWORD = '13ad24sf35dg'
#EMAIL_PORT = 587


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.kinghost.net'
#EMAIL_HOST_USER = 'agenciaoner.send@agenciaoner.com.br'
#EMAIL_HOST_PASSWORD = '13ad24sf35dg'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'default from email'

#EMAIL_HOST = 'smtp.sendgrid.net'
#EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
#EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'agenciaoner.send@agenciaoner.com.br'
SERVER_EMAIL = 'agenciaoner.send@agenciaoner.com.br'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.kinghost.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'agenciaoner.send@agenciaoner.com.br'
EMAIL_HOST_PASSWORD = '13ad24sf35dg'

#SERVER_EMAIL = 'agenciaoner.send@agenciaoner.com.br'
#EMAIL_USE_TLS = True

#EMAIL_HOST_PASSWORD = '13ad24sf35dg'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = "False"


#EMAIL_HOST = "smtp.gmail.com"
#EMAIL_HOST_USER = "upbankvendas@gmail.com"
##EMAIL_HOST_PASSWORD = "@Upbank2022"
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'default from email'


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



