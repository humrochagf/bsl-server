from bsl.core.models import User


def is_logged(cookie):
    user = User.objects.filter(token=cookie)

    if len(user) == 1:
        return True

    return False


def get_logged_user(cookie):
    return User.objects.filter(token=cookie)[0]


def authenticate(user, cookie):
    user.token = cookie
    user.save()


def invalidate(user):
    user.token = ''
    user.save()
