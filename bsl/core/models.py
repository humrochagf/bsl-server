# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    token = models.CharField(_('access token'), max_length=40, blank=True, null=True)
    last_token_auth = models.DateTimeField(_('last token authentication'), default=timezone.now)
