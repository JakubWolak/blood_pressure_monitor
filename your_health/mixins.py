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

    def get_context_data(self, **kwargs):
        """passes userdata to template"""

        context = super().get_context_data(**kwargs)
        try:
            userdata = UserData.objects.get(user=self.request.user)
        except UserData.DoesNotExist as e:
            print(e)
            userdata = None

        context['user'] = userdata
        
        return context


class UserDataExistsMixin:
    """
    checks if userdata does not exits, otherwise redirects to edit_userdata form
    """
    def dispatch(self, request, *args, **kwargs):
        try:
            UserData.objects.get(user=request.user)
        except UserData.DoesNotExist:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect(reverse('your_health:edit_data'))
    
    def get_context_data(self, **kwargs):
        """passes userdata to template"""

        context = super().get_context_data(**kwargs)
        try:
            userdata = UserData.objects.get(user=self.request.user)
        except UserData.DoesNotExist as e:
            print(e)
            userdata = None

        context['user'] = userdata
        
        return context