from django.shortcuts import render

from bsl.core.utils import generate_token, make_qrcode_base64


def login(request):
    token = generate_token()

    context = {'token': token, 'qrcode': make_qrcode_base64(token)}

    return render(request, 'core/login.html', context)

def barcode_login(request, token):
    # TODO: barcode_login
    context = {'token': token}

    return render(request, 'core/barcode_login.html', context)
