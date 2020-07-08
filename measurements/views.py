from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django_tables2 import SingleTableView

from .models import Measurement
from .forms import MeasurementCreateForm
from .tables import MeasurementTable
from your_health.mixins import UserDataRequiredMixin
from your_health.models import UserData


class MeasurementCreate(LoginRequiredMixin, UserDataRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = 'Zaloguj'

    template_name = 'measurements/measurement_create.html'
    success_url = reverse_lazy('measurements:show_measurements')

    model = Measurement
    form_class = MeasurementCreateForm

    def form_valid(self, form):
        measurement = form.save(commit=False)

        try:
            measurement.userdata = UserData.objects.get(user=self.request.user)
        except UserData.DoesNotExists:
            raise ValidatationError(_('Nie uzupełniono szczegółowych danych dla zalogowanego użytkownika'), code='invalid')

        return super(MeasurementCreate, self).form_valid(form)


class MeasurementTableView(LoginRequiredMixin, UserDataRequiredMixin, SingleTableView):
    template_name = 'measurements/measurement_list.html'
    context_object_name = 'table'

    table_class = MeasurementTable
    #model = Measurement

    def get_queryset(self):
        """returns measurements that belongs to logged user"""
        return Measurement.queryset_for_user(self.request.user)
