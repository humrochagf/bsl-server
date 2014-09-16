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
    if request.method == 'GET' and url_token:
        context = {'token': url_token}

        response = render(request, 'core/token_authentication.html', context)
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        token = request.POST.get('token')

        colision = authenticate(token=token)

        if not colision:
            user = authenticate(email=email, password=password)

            if user:
                if user.is_active:
                    user.token = token
                    user.save()
                    response = HttpResponse('Token autenticado!')
                else:
                    response = HttpResponse('Usuário inativo')
            else:
                response = HttpResponse('Falha ao autenticar token usuário ou senha incorreto')
        else:
            response = HttpResponse('Falha ao autenticar colisão de token encontrada')
    else:
        response = HttpResponseBadRequest()

    return response
