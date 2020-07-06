from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from measurements.mixins import UserDataRequiredMixin


class HomePageView(LoginRequiredMixin, UserDataRequiredMixin, TemplateView):
    template_name = 'homepage/index.html'
