from django_tables2 import Table, Column

from .models import Measurement


class MeasurementTable(Table):
    """class used to render table of all measurements"""
    id_mes = Column()

    class Meta:
        attrs = {'class': 'table table-striped'}
        model = Measurement
        fields = ('id_mes', 'measurement_time', 'systolic_pressure', 'diastolic_pressure', 'pulse')
