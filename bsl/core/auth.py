# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib.auth.backends import ModelBackend

from bsl.core.models import User


class CustomUserBackend(ModelBackend):
    def authenticate(self, email=None, password=None, token=None):
        if email and password and not token:
            user = super().authenticate(email=email, password=password)
        elif email and password and token:
            user = super().authenticate(email=email, password=password)
            if user:
                user.token = token
                user.save()
        elif not email and not password and token:
            try:
                user = User.objects.get(token)
            except ObjectDoesNotExist:
                user = None
            except MultipleObjectsReturned:
                user = None
        else:
            user = None

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None
