# -*- coding: utf-8 -*-
import os
import dj_database_url

from .base import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

SECRET_KEY = '&mc9cnu9q9io^hk^a%5!##+u1c#yp*50osoxca@%xc+h7$@!f8'

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///{0}'.format(os.path.join(BASE_DIR, 'db.sqlite3')))
}
