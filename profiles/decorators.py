from functools import wraps
from django.shortcuts import redirect


def unauthenticated_user(view_function):
    @wraps(view_function)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper
