from django.forms import ModelForm, Select, NumberInput, TextInput

from .models import UserData
from .choices import SEX


class UserDataForm(ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'surname', 'sex', 'height', 'weight']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control form-control-user',
            }),
            'surname': TextInput(attrs={
                'class': 'form-control form-control-user',
            }),
            'sex': Select(choices=SEX, attrs={
                'class': 'form-control form-control-user',
            }),
            'height': NumberInput(attrs={
                'class': 'form-control form-control-user',
            }),
            'weight': NumberInput(attrs={
                'class': 'form-control form-control-user',
            })
        }