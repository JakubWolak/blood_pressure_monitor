from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .decorators import userdata_does_not_exists
from measurements.mixins import UserDataRequiredMixin
from measurements.models import Measurement
from your_health.models import UserData


class HomePageView(LoginRequiredMixin, UserDataRequiredMixin, TemplateView):
    template_name = 'homepage/index.html'


@login_required
@userdata_does_not_exists
def get_data_for_charts(request, *args, **kwargs):
    """
    it returns JsonResponse object to generate charts in the homepage
    """
    pass
