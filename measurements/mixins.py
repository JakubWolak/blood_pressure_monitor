from django.shortcuts import redirect
from django.urls import reverse

from your_health.models import UserData


class UserDataRequiredMixin:
    """
    checks if userdata exists for request.user, otherwise redirects to add_data form
    """
    def dispatch(self, request, *args, **kwargs):
        try:
            UserData.objects.get(user=request.user)
        except UserData.DoesNotExist:
            return redirect(reverse('your_health:add_data'))
        
        return super().dispatch(request, *args, **kwargs)
