from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import UserData
from .choices import SEX


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'surname', 'sex', 'height', 'weight']

        widgets = {
            'sex': forms.Select(choices=SEX)
        }

        labels = {
            'name': _('Imię'),
            'surname': _('Nazwisko'),
            'sex': _('Płeć'),
            'height': _('Wzrost'),
            'weight': _('Waga'),
        }