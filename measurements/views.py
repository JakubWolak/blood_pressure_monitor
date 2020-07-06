from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Measurement
from .forms import MeasurementCreateForm

# TODO: add custom mixin  "must have UserData!!!"
class MeasurementCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = 'Zaloguj'

    template_name = 'measurements/measurement_create.html'
    success_url = reverse_lazy('measurements:show_measurements')

    model = Measurement
    form_class = MeasurementCreateForm


# TODO: add custom mixin "must have UserData!!!"
class MeasurementListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('acocunts:login')
    redirect_field_name = 'Zaloguj'

    template_name = 'measurements/measurement_list.html'

    model = Measurement
    paginate_by = 20
