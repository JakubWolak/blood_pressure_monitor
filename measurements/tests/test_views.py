from django.test import TestCase, Client

from django.contrib.auth.models import User
from your_health.models import UserData
from measurements.models import Measurement
from measurements.views import MeasurementCreateView, MeasurementTableView


class MeasurementCreateViewTest(TestCase):
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
