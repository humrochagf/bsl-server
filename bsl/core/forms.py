# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(label=_('Username'), max_length=30, required=False)
    password = forms.CharField(label=_('Password'), max_length=128, widget=forms.PasswordInput(), required=False)
    token = forms.CharField(max_length=40, widget=forms.HiddenInput())

    def update_token(self, token):
        data = self.data.copy()
        data['token'] = token
        self.data = data


class TokenAuthForm(forms.Form):
    username = forms.CharField(label=_('Username'), max_length=30)
    password = forms.CharField(label=_('Password'), max_length=128, widget=forms.PasswordInput())
    token = forms.CharField(max_length=40)
