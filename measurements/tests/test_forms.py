from django.test import TestCase

from django.contrib.auth.models import User
from your_health.models import UserData
from measurements.forms import MeasurementCreateForm


class MeasurementCreateFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="username",
            first_name="first_name",
            last_name="last_name",
            email="email@email.com",
            password="password",
            is_staff=False,
            is_active=True,
        )
        self.userdata = UserData(
            user=self.user,
            name=self.user.first_name,
            surname=self.user.last_name,
            sex="male",
            height=190,
            weight=90,
        )

    def test_valid_form(self):
        form_data = {
            "userdata": self.userdata,
            "systolic_pressure": 120,
            "diastolic_pressure": 80,
            "pulse": 60,
        }
        form = MeasurementCreateForm(form_data)

        self.assertTrue(form.is_valid())

    def test_systolic_pressure_required(self):
        form_data = {
            "userdata": self.userdata,
            "diastolic_pressure": 80,
            "pulse": 60,
        }
        form = MeasurementCreateForm(form_data)

        self.assertFalse(form.is_valid())

    def test_diastolic_pressure_required(self):
        form_data = {
            "userdata": self.userdata,
            "systolic_pressure": 120,
            "pulse": 60,
        }
        form = MeasurementCreateForm(form_data)

        self.assertFalse(form.is_valid())

    def test_pulse_required(self):
        form_data = {
            "userdata": self.userdata,
            "systolic_pressure": 120,
            "diastolic_pressure": 80,
        }
        form = MeasurementCreateForm(form_data)

        self.assertFalse(form.is_valid())
