from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from measurements.mixins import UserDataRequiredMixin
from measurements.models import Measurement
from your_health.models import UserData


class HomePageView(LoginRequiredMixin, UserDataRequiredMixin, TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # getting measurements for logged user
        # mixin provides that this won't throw an exception
        userdata = UserData.objects.get(user=self.request.user)
        context['measurements'] = Measurement.objects.filter(userdata=userdata)

        return context
