from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from your_health.mixins import UserDataRequiredMixin

from your_health.models import UserData
from your_doctor.models import DoctorData
from your_doctor.forms import DoctorDataForm


class DoctorDataCreateView(LoginRequiredMixin, UserDataRequiredMixin, CreateView):
    template_name = "your_doctor/add_doctordata.html"
    success_url = reverse_lazy("homepage:index")

    model = DoctorData
    form_class = DoctorDataForm

    def form_valid(self, form):
        doctordata = form.save(commit=False)
        userdata = UserData.objects.get(user=self.request.user)
        doctordata.userdata = userdata

        messages.add_message(
            self.requets, messages.INFO, "Pomyślnie zaktualizowano dane"
        )

        return super(DoctorDataCreateView, self).form_valid(form)


class DoctorDataUpdateView(LoginRequiredMixin, UserDataRequiredMixin, UpdateView):
    model = Doctor
    form_class = DoctorDataForm

    template_name = "your_doctor/add_data.html"
    success_url = reverse_lazy("homepage:index")

    def get_initial(self):
        initial = {}

        try:
            usserdata = UserData.objects.get(user=self.request.user)


