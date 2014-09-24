# -*- coding: utf-8 -*-
ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'core.User'

AUTHENTICATION_BACKENDS = ('bsl.core.backends.CustomUserBackend',)

LOGIN_URL = '/login/'

LOGOUT_URL = '/logout/'

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'bsl.core',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bsl.urls'

WSGI_APPLICATION = 'bsl.wsgi.application'

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
