from django.test import TestCase

from django.contrib.auth.models import User
from your_health.models import UserData
from measurements.models import Measurement


class MeasurementTest(TestCase):
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
        self.userdata = UserData.objects.create(
            user=self.user,
            name=self.user.first_name,
            surname=self.user.last_name,
            sex="male",
            height=190,
            weight=90,
        )
        self.measurement = Measurement.objects.create(
            userdata=self.userdata,
            systolic_pressure=120,
            diastolic_pressure=80,
            pulse=60,
        )

    def test_data_correctness(self):
        self.assertEqual(self.measurement.userdata, self.userdata)
        self.assertEqual(self.measurement.systolic_pressure, 120)
        self.assertEqual(self.measurement.diastolic_pressure, 80)
        self.assertEqual(self.measurement.pulse, 60)

    def test_get_queryset_for_user(self):
        measurement_object = self.measurement.queryset_for_user(self.user)[0]

        self.assertTrue(measurement_object)
        self.assertEqual(measurement_object.userdata, self.userdata)

    def test_str_method(self):
        expected_string = "Pomiar dla: {user}, wynik: {systolic}/{diastolic}, tętno: {pulse}".format(
            user=self.userdata.get_full_name(),
            systolic=self.measurement.systolic_pressure,
            diastolic=self.measurement.diastolic_pressure,
            pulse=self.measurement.pulse,
        )

        self.assertEqual(self.measurement.__str__(), expected_string)
