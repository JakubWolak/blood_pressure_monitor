from django.test import TestCase

from django.contrib.auth.models import User
from your_health.models import UserData
from your_doctor.models import DoctorData


class TestDoctorDataModel(TestCase):
    def setUp(self):
        self.user = User(
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
        self.doctordata = DoctorData(
            userdata=self.userdata,
            name="name",
            surname="surname",
            email="email@email.com",
        )

    def test_data_correctness(self):
        self.assertEqual(self.doctordata.userdata, self.userdata)
        self.assertEqual(self.doctordata.name, "name")
        self.assertEqual(self.doctordata.surname, "surname")
        self.assertEqual(self.doctordata.email, "email@email.com")

    def test_get_full_name_method(self):
        expected_string = "name surname"
        self.assertEqual(self.doctordata.get_full_name(), expected_string)

    def test_str_method(self):
        expected_string = "Kardiolog name surname"
        self.assertEqual(self.doctordata.__str__(), expected_string)
