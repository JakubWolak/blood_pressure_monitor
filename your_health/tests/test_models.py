from django.test import TestCase

from django.contrib.auth.models import User
from your_health.models import UserData


class TestUserDataModel(TestCase):
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

    def test_data_correctness(self):
        self.assertEqual(self.userdata.user, self.user)
        self.assertEqual(self.userdata.name, "first_name")
        self.assertEqual(self.userdata.surname, "last_name")
        self.assertEqual(self.userdata.sex, "male")
        self.assertEqual(self.userdata.height, 190)
        self.assertEqual(self.userdata.weight, 90)

    def test_get_full_name_method(self):
        expected_string = self.userdata.name + " " + self.userdata.surname
        self.assertEqual(self.userdata.get_full_name(), expected_string)

    def test_str_method(self):
        expected_string = "Użytkownik {fullname}, płeć {sex}, wzrost {height}, waga {weight}".format(
            fullname=self.userdata.get_full_name(),
            sex=self.userdata.sex,
            height=self.userdata.height,
            weight=self.userdata.weight,
        )
        self.assertEqual(self.userdata.__str__(), expected_string)
