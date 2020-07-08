from django_tables2 import Table

from .models import Measurement


class MeasurementTable(Table):
    """class used to render table of all measurements"""
    class Meta:
        model = Measurement
        fields = ('measurement_time','systolic_pressure', 'diastolic_pressure', 'pulse')