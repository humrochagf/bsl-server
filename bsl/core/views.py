from base64 import b64encode
from hashlib import sha1
from io import BytesIO
from os import urandom

import qrcode
from django.shortcuts import render

# --- Done now
from django.http import HttpResponse
from django.http import Http404
from bsl.core import auth
from bsl.core.models import Usuario
# ---

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

    # Create response
    response = HttpResponse()

    response = render(request, 'core/login.html', context)

    # Set cookie to be authenticated
    response.set_cookie(key='auth', value=token)

    return response

def barcode_login(request):
    # request.COOKIES["auth"]
    # context = {'auth_cookie': request.COOKIES["auth"], 'message': user.senha}
    # return render(request, 'core/barcode_login.html', context)

    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        u = Usuario.objects.get(email=request.POST['username'])
        if u.senha == request.POST['password']:
            auth.authenticate(u, request.POST["auth_cookie"])
            return HttpResponse("You are logged in!!! =]~")
            # return HttpResponseRedirect('/you-are-logged-in/')
        else:
            return HttpResponse("Your username and password didn't match.")
    except Usuario.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")

def barcode_loggoff(request):
    u = auth.get_logged_user(request.COOKIES["auth"])
    auth.invalidate(u)
    return HttpResponse("You are logged off, buy.")

def restricted_area(request):
    if auth.is_logged(request.COOKIES["auth"]):
        u = auth.get_logged_user(request.COOKIES["auth"])
        return HttpResponse("Welcome " + u.nome + ", this is a restricted area!")
    else:
        return HttpResponse("This is a restricted area, you need to authenticate!")

def mobile_simulation(request):
    return render(request, 'core/mobile_simulation.html')