from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Measurement

# TODO: add custom mixin  "must have UserData!!!"
class MeasurementCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = 'Zaloguj'

    template_name = 'measurements/measurement_create.html'
    success_url = reverse_lazy('homepage:index')

    model = Measurement
    fields = ['systolic_pressure', 'diastolic_pressure', 'pulse']
