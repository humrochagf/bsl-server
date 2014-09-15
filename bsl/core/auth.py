from bsl.core.models import Usuario

def is_logged(cookie):
    user = Usuario.objects.filter(auth=cookie)

    if len(user) > 0 and len(user) < 2:
        return True

    return False

def get_logged_user(cookie):
    return Usuario.objects.filter(auth=cookie)[0]

def authenticate(user, cookie):
    user.auth = cookie
    user.save()

def invalidate(user):
    user.auth = ''
    user.save()