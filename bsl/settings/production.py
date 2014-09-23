# -*- coding: utf-8 -*-
import dj_database_url

from . import get_env_variable
from .base import *


SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

MIDDLEWARE_CLASSES += ('sslify.middleware.SSLifyMiddleware', )

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

DATABASES = {
    'default': dj_database_url.config()
}
