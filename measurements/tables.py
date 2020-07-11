from django_tables2 import Table, Column
from django.utils.html import mark_safe, escape
import datetime

from .models import Measurement
from .pressure_values import systolic_pressure, diastolic_pressure, pulse, css_classes


class MeasurementTable(Table):
    """class used to render table of all measurements"""

    systolic_pressure = Column()
    diastolic_pressure = Column()
    pulse = Column()

    class Meta:
        attrs = {"class": "table"}
        model = Measurement
        fields = (
            "measurement_time",
            "systolic_pressure",
            "diastolic_pressure",
            "pulse",
        )

    def render_systolic_pressure(self, value):
        """adds class depends on value"""
        min_val = systolic_pressure["min"]
        max_val = systolic_pressure["max"]
        good = css_classes["good"]
        bad = css_classes["bad"]

        if value > max_val or value < min_val:
            return generate_return(bad, value)
        else:
            return generate_return(good, value)

    def render_diastolic_pressure(self, value):
        """adds class depends on value"""
        min_val = diastolic_pressure["min"]
        max_val = diastolic_pressure["max"]
        good = css_classes["good"]
        bad = css_classes["bad"]

        if value > max_val or value < min_val:
            return generate_return(bad, value)
        else:
            return generate_return(good, value)

    def render_pulse(self, value):
        """adds class depends on value"""
        min_val = pulse["min"]
        max_val = pulse["max"]
        good = css_classes["good"]
        bad = css_classes["bad"]

        if value > max_val or value < min_val:
            return generate_return(bad, value)
        else:
            return generate_return(good, value)


def generate_return(css_class, value):
    """ returns value for render_ method """
    return mark_safe(
        "<span class='{css_class}'>{value}</span>".format(
            css_class=escape(css_class), value=escape(value)
        )
    )
