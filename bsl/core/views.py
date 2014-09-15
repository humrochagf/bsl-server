from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate

from bsl.core.utils import generate_token, make_qrcode_base64
from bsl.core import auth


def login(request):
    if request.method == 'GET':
        token = generate_token()

        context = {'token': token, 'qrcode': make_qrcode_base64(token)}

        response = render(request, 'core/login.html', context)

        return response
    else:
        return HttpResponse('Not implemented yet')


def barcode_login(request):
    # request.COOKIES["auth"]
    # context = {'auth_cookie': request.COOKIES["auth"], 'message': user.senha}
    # return render(request, 'core/barcode_login.html', context)

    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')

    email = request.POST['username']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user is not None:
        if user.is_active:
            # TODO: Mudar para django auth.login
            auth.authenticate(user, request.POST["token"])

            response = HttpResponse("You are logged in!!! =]~")
            response.set_cookie(key='token', value=request.POST['token'])

            return response
        else:
            return HttpResponse('The user is inactive')
    else:
        return HttpResponse("Your username and password didn't match.")


def barcode_loggoff(request):
    # TODO: Mudar para auth logout
    # metodo atual permite desconectar qualquer usuário sabendo seu token

    user = auth.get_logged_user(request.COOKIES["token"])
    auth.invalidate(user)
    return HttpResponse("You are logged off, buy.")


def restricted_area(request):
    # TODO: Mudar para o auth check do django, criar um custom authentication backend

    if auth.is_logged(request.COOKIES["token"]):
        user = auth.get_logged_user(request.COOKIES["token"])
        return HttpResponse("Welcome " + user.get_full_name() + ", this is a restricted area!")
    else:
        return HttpResponse("This is a restricted area, you need to authenticate!")


def mobile_simulation(request):
    return render(request, 'core/mobile_simulation.html')
