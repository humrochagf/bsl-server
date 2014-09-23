# -*- coding: utf-8 -*-
import django.contrib.auth as auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from bsl.core.helpers import generate_token, make_qrcode_base64
from bsl.core.forms import LoginForm, TokenAuthForm


def index(request):
    return redirect('/login/')


def login(request):
    template = 'core/login.html'
    token = generate_token()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.authenticate()

            if user:
                user.token = None
                user.save()
                auth.login(request, user)
                return redirect('/restricted/')

        form.update_token(token)
    else:
        form = LoginForm()
        form.fields['token'].initial = token

    auth_token_page = request.build_absolute_uri(reverse('auth_token', args=(token, )))

    context = dict(qrcode=make_qrcode_base64(auth_token_page), form=form)

    return render(request, template, context)


@login_required()
def logout(request):
    auth.logout(request)

    return redirect('/login/')


def token_authentication(request, url_token=None):
    template = 'core/token_authentication.html'
    success = False

    if request.method == 'POST':
        form = TokenAuthForm(request.POST)

        if form.is_valid():
            user = form.authenticate()

            if user:
                user.token = form.cleaned_data['token']
                user.save()
                success = True
    else:
        form = TokenAuthForm()
        form.fields['token'].initial = url_token

    context = dict(success=success, token=url_token, form=form)

    return render(request, template, context)


@login_required()
def restricted_area(request):
    template = 'core/restricted_area.html'

    return render(request, template)
