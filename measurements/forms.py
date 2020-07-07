from django.forms import ModelForm, NumberInput

from .models import Measurement


class MeasurementCreateForm(ModelForm):
    class Meta:
        model = Measurement
        fields = ['systolic_pressure', 'diastolic_pressure', 'pulse']

        widgets = {
            'systolic_pressure': NumberInput(attrs={
                'class': 'form-control form-control-user',
            }),
            'diastolic_pressure': NumberInput(attrs={
                'class': 'form-control form-control-user',
            }),
            'pulse': NumberInput(attrs={
                'class': 'form-control form-control-user',
            })
        }