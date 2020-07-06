from django.shortcuts import redirect
from django.urls import reverse

from your_health.models import UserData


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