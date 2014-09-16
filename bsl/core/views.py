# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

from bsl.core.utils import generate_token, make_qrcode_base64


def login_page(request, url_token=None):
    if request.method == 'GET':
        if not url_token:  # Página principal de login
            token = generate_token()

            context = {'qrcode': make_qrcode_base64(token)}

            response = render(request, 'core/login.html', context)

        else:  # Página de login com o token escaneado
            context = {'token': url_token}

            response = render(request, 'core/barcode_login.html', context)
    else:
        email = request.POST.get('username')
        password = request.POST.get('password')
        token = request.POST.get('token')

        print(email)
        print(password)
        print(token)

        user = authenticate(email=email, password=password, token=token)

        if user:
            if user.is_active:
                response = HttpResponse("You are logged in!!! =]~")
            else:
                response = HttpResponse('The user is inactive')
        else:
            response = HttpResponse("Your username and password didn't match.")

    return response
