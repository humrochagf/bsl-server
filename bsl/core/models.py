# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, first_name, last_name, password,
                     is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None,
                    **extra_fields):
        return self._create_user(email, first_name, last_name, password, False, True, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password,
                         **extra_fields):
        return self._create_user(email, first_name, last_name, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('endereço de email'), max_length=254, unique=True)
    first_name = models.CharField(_('nome'), max_length=30, blank=True)
    last_name = models.CharField(_('sobrenome'), max_length=60, blank=True)
    is_admin = models.BooleanField(_('status de staff'), default=False)
    is_active = models.BooleanField(_('ativo'), default=True)
    date_joined = models.DateTimeField(_('criado em'), default=timezone.now())
    token = models.CharField(_('token de acesso'), max_length=40, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')

    def get_full_name(self):
        full_name = '{0} {1}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Implementar para permissões adicionais
        return True

    def has_module_perms(self, app_label):
        # Implementar para permissões sobre módulos específicos
        return True

    @property
    def is_staff(self):
        # Implementar para níveis diferentes de admins
        return self.is_admin
