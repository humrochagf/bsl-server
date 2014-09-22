# -*- coding: utf-8 -*-
from django import forms
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    email = forms.EmailField(label=_('E-mail'), max_length=254, required=False)
    password = forms.CharField(label=_('Senha'), max_length=32, widget=forms.PasswordInput(), required=False)
    token = forms.CharField(max_length=40, widget=forms.HiddenInput())

    def update_token(self, token):
        data = self.data.copy()
        data['token'] = token
        self.data = data

    def authenticate(self):
        user = auth.authenticate(email=self.cleaned_data['email'],
                                 password=self.cleaned_data['password'],
                                 token=self.cleaned_data['token'])

        if user:
            user.token = None
            user.save()
            if user.is_active:
                return user
            else:
                # TODO: Transformar em slug
                # context.update(error='Usuário inativo')
                return None
        else:
            # TODO: Transformar em slug
            # context.update(error='Não foi possível logar...')
            return None


class TokenAuthForm(forms.Form):
    email = forms.EmailField(label=_('E-mail'), max_length=254)
    password = forms.CharField(label=_('Senha'), max_length=32, widget=forms.PasswordInput())
    token = forms.CharField(max_length=40)

    def authenticate(self):
        user = auth.authenticate(email=self.cleaned_data['email'],
                                 password=self.cleaned_data['password'])

        if user:
            if user.is_active:
                user.token = self.cleaned_data['token']
                user.save()
                return user
            else:
                # TODO: Transformar em slug
                # context.update(error='Usuário inativo')
                return None
        else:
            # TODO: Transformar em slug
            #context.update(error='Falha ao autenticar token: usuário ou senha incorreto')
            return None