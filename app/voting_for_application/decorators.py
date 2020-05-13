from django.shortcuts import redirect


def sensors_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.account.musician_or_sensor == 'SS':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_function
