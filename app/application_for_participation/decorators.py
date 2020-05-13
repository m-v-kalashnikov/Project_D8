from django.shortcuts import redirect


def musician_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.account.musician_or_sensor == 'MC':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_function
