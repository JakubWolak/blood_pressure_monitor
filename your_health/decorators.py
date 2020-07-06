from django.shortcuts import redirect
from django.urls import reverse

from .models import UserData


def userdata_does_not_exists(func):
    """
    checks if userdata exists for user, otherwise redirects to page with form to add this data
    """
    def check_and_call(request, *args, **kwargs):
        try:
            UserData.objects.get(user=request.user)
        except:
            return redirect(reverse('your_health:add_data'))

        return func(request, *args, **kwargs)
    return check_and_call


def userdata_exists(func):
    """
    checks if userdata exists for user, if data exists, redirects to view that allows to edit this data
    """
    def check_and_call(request, *args, **kwargs):
        try:
            UserData.objects.get(user=request.user)
        except:
            return func(request, *args, **kwargs)

        return redirect(reverse('your_health:edit_data'))
        
    return check_and_call