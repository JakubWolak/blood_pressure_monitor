from django.test import TestCase, Client

from django.shortcuts import reverse


from django.contrib.auth.models import User
from your_health.models import UserData
from measurements.models import Measurement

from measurements.views import MeasurementCreateView, MeasurementTableView


class CreateUserdata:
    @classmethod
    def create_user(self):
        user = User.objects.create_user(
            username="username",
            first_name="first_name",
            last_name="last_name",
            email="email@email.com",
            password="password",
            is_staff=False,
            is_active=True,
        )
        return user

    @classmethod
    def create_userdata(self, user):
        userdata = UserData.objects.create(
            user=user,
            name=user.first_name,
            surname=user.last_name,
            sex="male",
            height=190,
            weight=90,
        )
        return userdata


class MeausrementCreateViewTest(CreateUserdata, TestCase):
    def setUp(self):
        self.user = self.create_user()

        self.client = Client()

    def test_redirect_when_logged_out(self):
        response = self.client.get(reverse("measurements:add_measurement"), follow=True)

        self.assertEqual(
            response.redirect_chain[0][0],
            "/accounts/login/?next=/measurements/add_measurement",
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)

    def test_displaying_data_when_logged_in_without_userdata(self):
        self.client.login(username="username", password="password")
        response = self.client.get(reverse("measurements:add_measurement"), follow=True)
        messages = list(response.context["messages"])

        self.assertEqual(
            response.redirect_chain[0][0], "/your_health/add_data",
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["PATH_INFO"], reverse("your_health:add_data"))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Uzupełnij swoje dane")

    def test_displaying_data_when_logged_in_with_userdata(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.get(reverse("measurements:add_measurement"), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("measurements:add_measurement")
        )

    def test_messages_when_new_measurement_added(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.post(
            reverse("measurements:add_measurement"),
            {
                "userdata": userdata,
                "systolic_pressure": 120,
                "diastolic_pressure": 80,
                "pulse": 60,
            },
            follow=True,
        )
        messages = list(response.context["messages"])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("measurements:show_measurements")
        )
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Pomyślnie dodano pomiar")

    def test_messages_invalid_systolic_pressure(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.post(
            reverse("measurements:add_measurement"),
            {
                "userdata": userdata,
                "systolic_pressure": 131,
                "diastolic_pressure": 80,
                "pulse": 60,
            },
            follow=True,
        )
        messages = list(response.context["messages"])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("measurements:show_measurements")
        )
        self.assertEqual(len(messages), 2)
        self.assertEqual(
            str(messages[1]), "Twoje ciśnienie skurczowe jest nieprawidłowe"
        )

        response = self.client.post(
            reverse("measurements:add_measurement"),
            {
                "userdata": userdata,
                "systolic_pressure": 89,
                "diastolic_pressure": 80,
                "pulse": 60,
            },
            follow=True,
        )
        messages = list(response.context["messages"])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("measurements:show_measurements")
        )
        self.assertEqual(len(messages), 2)
        self.assertEqual(
            str(messages[1]), "Twoje ciśnienie skurczowe jest nieprawidłowe"
        )

    def test_messages_invalid_diastolic_pressure(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.post(
            reverse("measurements:add_measurement"),
            {
                "userdata": userdata,
                "systolic_pressure": 120,
                "diastolic_pressure": 96,
                "pulse": 60,
            },
            follow=True,
        )
        messages = list(response.context["messages"])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("measurements:show_measurements")
        )
        self.assertEqual(len(messages), 2)
        self.assertEqual(
            str(messages[1]), "Twoje ciśnienie rozkurczowe jest nieprawidłowe"
        )

        response = self.client.post(
            reverse("measurements:add_measurement"),
            {
                "userdata": userdata,
                "systolic_pressure": 120,
                "diastolic_pressure": 69,
                "pulse": 60,
            },
            follow=True,
        )
        messages = list(response.context["messages"])

        self.assertEqual(len(messages), 2)
        self.assertEqual(
            str(messages[1]), "Twoje ciśnienie rozkurczowe jest nieprawidłowe"
        )

    def test_messages_invalid_pulse(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.post(
            reverse("measurements:add_measurement"),
            {
                "userdata": userdata,
                "systolic_pressure": 120,
                "diastolic_pressure": 80,
                "pulse": 81,
            },
            follow=True,
        )
        messages = list(response.context["messages"])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("measurements:show_measurements")
        )
        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[1]), "Twoje tętno jest nieprawidłowe")

        response = self.client.post(
            reverse("measurements:add_measurement"),
            {
                "userdata": userdata,
                "systolic_pressure": 120,
                "diastolic_pressure": 80,
                "pulse": 81,
            },
            follow=True,
        )
        messages = list(response.context["messages"])

        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[1]), "Twoje tętno jest nieprawidłowe")


class MeasurementTableView(CreateUserdata, TestCase):
    def setUp(self):
        self.user = self.create_user()

        self.client = Client()

    def test_redirect_when_logged_out(self):
        response = self.client.get(
            reverse("measurements:show_measurements"), follow=True
        )

        self.assertEqual(
            response.redirect_chain[0][0],
            "/accounts/login/?next=/measurements/show_measurements",
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)

    def test_displaying_data_when_logged_in_without_userdata(self):
        self.client.login(username="username", password="password")
        response = self.client.get(reverse("measurements:add_measurement"), follow=True)
        messages = list(response.context["messages"])

        self.assertEqual(
            response.redirect_chain[0][0], "/your_health/add_data",
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["PATH_INFO"], reverse("your_health:add_data"))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Uzupełnij swoje dane")

    def test_displaying_data_when_logged_in_with_userdata(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.get(reverse("measurements:show_measurements"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("measurements:show_measurements")
        )
