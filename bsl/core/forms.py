# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    email = forms.EmailField(label=_('E-mail'), max_length=254, required=False)
    password = forms.CharField(label=_('Senha'), max_length=32, widget=forms.PasswordInput(), required=False)
    token = forms.CharField(max_length=40, widget=forms.HiddenInput())

    def update_token(self, token):
        data = self.data.copy()
        data['token'] = token
        self.data = data


class TokenAuthForm(forms.Form):
    email = forms.EmailField(label=_('E-mail'), max_length=254)
    password = forms.CharField(label=_('Senha'), max_length=32, widget=forms.PasswordInput())
    token = forms.CharField(max_length=40)
