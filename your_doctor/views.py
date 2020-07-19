from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from your_health.mixins import UserDataRequiredMixin
from your_doctor.mixins import DoctorDataExistsMixin, DoctorDataRequiredMixin

from your_health.models import UserData
from your_doctor.models import DoctorData
from your_doctor.forms import DoctorDataForm


class DoctorDataCreateView(
    LoginRequiredMixin, UserDataRequiredMixin, DoctorDataExistsMixin, CreateView
):
    template_name = "your_doctor/add_doctordata.html"
    success_url = reverse_lazy("homepage:index")

    model = DoctorData
    form_class = DoctorDataForm

    def form_valid(self, form):
        doctordata = form.save(commit=False)
        userdata = UserData.objects.get(user=self.request.user)
        doctordata.userdata = userdata

        messages.add_message(
            self.request, messages.INFO, "Pomyślnie zaktualizowano dane lekarza"
        )

        return super(DoctorDataCreateView, self).form_valid(form)


class DoctorDataUpdateView(
    LoginRequiredMixin, UserDataRequiredMixin, DoctorDataRequiredMixin, UpdateView
):
    model = DoctorData
    form_class = DoctorDataForm

    template_name = "your_doctor/add_doctordata.html"
    success_url = reverse_lazy("homepage:index")

    def get_initial(self):
        initial = {}

        try:
            userdata = UserData.objects.get(user=self.request.user)
            doctordata = DoctorData.objects.get(userdata=userdata)
            initial["name"] = doctordata.name
            initial["surname"] = doctordata.surname
            initial["email"] = doctordata.email
        except DoctorData.DoesNotExist as e:
            print(e)
            initial = {}

        return initial

    def get_object(self):
        try:
            userdata = UserData.objects.get(user=self.request.user)
            obj = DoctorData.objects.get(userdata=userdata)
        except:
            obj = None

        return obj

    def form_valid(self, form):
        userdata = form.save()

        messages.add_message(
            self.request, messages.INFO, "Pomyślnie zaktualizowano dane lekarza"
        )

        return super(DoctorDataUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.WARNING, "Niepoprawnie wypełniony formularz"
        )

        return redirect(reverse("your_doctor:edit_data"))

