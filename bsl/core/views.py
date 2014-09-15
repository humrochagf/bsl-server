from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from bsl.core.utils import generate_token, make_qrcode_base64
from bsl.core import auth
from bsl.core.models import Usuario


def login(request):
    token = generate_token()

    context = {'token': token, 'qrcode': make_qrcode_base64(token)}

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
