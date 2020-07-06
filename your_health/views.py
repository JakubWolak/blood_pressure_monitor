from django.contrib.auth.mixins import LoginRequiredMixin
from your_health.mixins import UserDataRequiredMixin, UserDataExistsMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import UserDataForm
from .models import UserData


class UserDataCreate(LoginRequiredMixin, UserDataExistsMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    redirect_field_name = 'Zaloguj'

    template_name = 'your_health/add_userdata.html'
    success_url = reverse_lazy('homepage:index')

    model = UserData
    form_class = UserDataForm

    def form_valid(self, form):
        userdata = form.save(commit=False)
        userdata.user = self.request.user

        return super(UserDataCreate, self).form_valid(form)


class UserDataUpdate(LoginRequiredMixin, UserDataRequiredMixin, CreateView):
    model = UserData
    fields = ['name', 'surname', 'sex', 'height', 'weight']

    template_name = 'your_health/add_userdata.html'
