# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib.auth.backends import ModelBackend

from .models import User


class CustomUserBackend(ModelBackend):
    def authenticate(self, username=None, password=None, token=None):
        user = super().authenticate(username=username, password=password)

        if not user and token:
            try:
                user = User.objects.get(token=token)
                if user.get_token_age() > 60:
                    user = None
            except ObjectDoesNotExist:
                user = None
            except MultipleObjectsReturned:
                user = None

        return user
