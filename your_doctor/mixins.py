from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

from your_health.models import UserData
from your_doctor.models import DoctorData


class DoctorDataRequiredMixin:
    """
    checks if doctordata exists for userdata, otherwise redirects to add_data form
    """

    def dispatch(self, request, *args, **kwargs):
        try:
            userdata = UserData.objects.get(user=request.user)
            DoctorData.objects.get(userdata=userdata)
        except:
            messages.add_message(
                self.request, messages.WARNING, "Uzupełnij dane swojego lekarza"
            )
            return redirect(reverse("your_doctor:add_data"))

        return super().dispatch(request, *args, **kwargs)


class DoctorDataExistsMixin:
    """
    checks if doctordata does not exist, otherwise redirects to edit_doctordata form
    """

    def dispatch(self, request, *args, **kwargs):
        try:
            userdata = UserData.objects.get(user=request.user)
            DoctorData.objects.get(userdata=userdata)
        except:
            return super().dispatch(request, *args, **kwargs)

        return redirect(reverse("your_doctor:add_data"))

