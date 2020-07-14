from django.contrib.auth.mixins import LoginRequiredMixin
from your_health.mixins import UserDataRequiredMixin, UserDataExistsMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import UserDataForm
from .models import UserData


class UserDataCreateView(LoginRequiredMixin, UserDataExistsMixin, CreateView):
    template_name = "your_health/add_userdata.html"
    success_url = reverse_lazy("homepage:index")

    model = UserData
    form_class = UserDataForm

    def form_valid(self, form):
        userdata = form.save(commit=False)
        userdata.user = self.request.user

        messages.add_message(
            self.request, messages.INFO, "Pomyślnie zaktualizowano dane"
        )

        return super(UserDataCreateView, self).form_valid(form)


class UserDataUpdateView(LoginRequiredMixin, UserDataRequiredMixin, UpdateView):
    model = UserData
    form_class = UserDataForm

    template_name = "your_health/add_userdata.html"
    success_url = reverse_lazy("homepage:index")

    def get_initial(self):
        initial = {}

        try:
            userdata = UserData.objects.get(user=self.request.user)
            initial["name"] = userdata.name
            initial["surname"] = userdata.surname
            initial["sex"] = userdata.sex
            initial["height"] = userdata.height
            initial["weight"] = userdata.weight
        except UserData.DoesNotExist as e:
            print(e)
            initial = {}

        return initial

    def get_object(self):
        try:
            obj = UserData.objects.get(user=self.request.user)
        except UserData.DoesNotExist:
            obj = None

        return obj

    def form_valid(self, form):
        userdata = form.save()

        messages.add_message(
            self.request, messages.INFO, "Pomyślnie zaktualizowano dane"
        )

        return super(UserDataUpdateView, self).form_valid(form)
