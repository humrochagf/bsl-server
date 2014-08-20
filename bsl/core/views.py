from base64 import b64encode
from hashlib import sha1
from io import BytesIO
from os import urandom

import qrcode
from django.shortcuts import render


def login(request):
    # Generate the nonce
    # TODO: Work on the entropy and size of the nonce
    token = sha1(urandom(128)).hexdigest()

    # Create a temporary placeholder to the image
    stream = BytesIO()

    # Generate the qrcode and save to the stream
    qrcode.make(token).save(stream)

    # Get the image bytes, then encode to base64
    data = b64encode(stream.getvalue())

    context = {'token': token, 'qrcode': data}

    return render(request, 'core/login.html', context)

def barcode_login(request, token):
    # TODO: barcode_login
    context = {'token': token}

    return render(request, 'core/barcode_login.html', context)
