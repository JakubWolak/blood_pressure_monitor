from django.forms import ModelForm, TextInput, EmailInput

from .models import DoctorData


class DoctorDataForm(ModelForm):
    class Meta:
        model = DoctorData
        fields = ["name", "surname", "email"]

        widgets = {
            "name": TextInput(attrs={"class": "form-control form-control-user",}),
            "surname": TextInput(attrs={"class": "form-control form-control-user",}),
            "email": EmailInput(attrs={"class": "form-control form-control-user",}),
        }
