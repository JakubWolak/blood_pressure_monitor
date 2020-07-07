from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from your_health.mixins import UserDataRequiredMixin


class HomePageView(LoginRequiredMixin, UserDataRequiredMixin, TemplateView):
    template_name = 'homepage/index.html'


class SystolicPressureView(LoginRequiredMixin, UserDataRequiredMixin, TemplateView):
    template_name = 'homepage/systolic_pressure.html'


class DiastolicPressureView(LoginRequiredMixin, UserDataRequiredMixin, TemplateView):
    template_name = 'homepage/diastolic_pressure.html'


class PulseView(LoginRequiredMixin, UserDataRequiredMixin, TemplateView):
    template_name = 'homepage/pulse.html'
