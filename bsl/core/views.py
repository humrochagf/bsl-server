# -*- coding: utf-8 -*-
import django.contrib.auth as auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from bsl.core.helpers import generate_token, make_qrcode_base64
from bsl.core.forms import LoginForm


def login(request):
    # BUG: Token not updating correctly
    template = 'core/login.html'
    token = generate_token()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = form.authenticate()

            if user:
                auth.login(request, user)
                return redirect('/restricted/')

        form.update_token(token)
    else:
        form = LoginForm()

    context = dict(qrcode=make_qrcode_base64(token), form=form)

    return render(request, template, context)


@login_required()
def logout(request):
    auth.logout(request)

    return redirect('/login/')


def token_authentication(request, url_token=None):
    template = 'core/token_authentication.html'
    context = {'token': url_token}

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        token = request.POST.get('token')

        user = auth.authenticate(email=email, password=password)

        if user:
            if user.is_active:
                user.token = token
                user.save()
                context.update(success=True)
            else:
                context.update(error='Usuário inativo')
        else:
            context.update(error='Falha ao autenticar token: usuário ou senha incorreto')

    return render(request, template, context)


@login_required()
def restricted_area(request):
    template = 'core/restricted_area.html'

    return render(request, template)
