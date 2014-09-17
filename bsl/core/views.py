# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate

from bsl.core.utils import generate_token, make_qrcode_base64


def login(request):
    if request.method == 'GET':
        token = generate_token()

        context = {'qrcode': make_qrcode_base64(token), 'token': token}

        response = render(request, 'core/login.html', context)
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        token = request.POST.get('token')

        user = authenticate(email=email, password=password, token=token)
        
        if user:
            if user.is_active:
                response = HttpResponse('Usuário {0} logado com sucesso!'.format(user.get_full_name()))
            else:
                response = HttpResponse('Usuário inativo')
        else:
            response = HttpResponse('Não foi possível logar...')
    else:
        response = HttpResponseBadRequest()

    return response


def token_authentication(request, url_token=None):
    template = 'core/token_authentication.html'
    context = {'token': url_token,
               'error': None,
               'success': False}

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        token = request.POST.get('token')

        user = authenticate(email=email, password=password)

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
