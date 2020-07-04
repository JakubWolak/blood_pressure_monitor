from django import forms

from .models import UserData
from .choices import SEX


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'surname', 'sex', 'height', 'weight']

        widgets = {
            'sex': forms.Select(choices=SEX)
        }