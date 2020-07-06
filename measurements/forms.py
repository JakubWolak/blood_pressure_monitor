from django import forms

from .models import Measurement


class MeasurementCreateForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['systolic_pressure', 'diastolic_pressure', 'pulse']