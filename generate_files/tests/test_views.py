from django.test import TestCase, Client
import csv
import io

from django.shortcuts import reverse

from django.contrib.auth.models import User
from your_health.models import UserData
from measurements.models import Measurement


class CreateUserData:
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

    @classmethod
    def create_measurement(self, userdata):
        measurement = Measurement.objects.create(
            userdata=userdata, systolic_pressure=120, diastolic_pressure=80, pulse=60,
        )
        return measurement

    class Meta:
        abstract = True


class GenerateFilesMenuView(CreateUserData, TestCase):
    def setUp(self):
        self.user = self.create_user()

        self.client = Client()

    def test_redirect_when_logged_out(self):
        response = self.client.get(reverse("generate_files:menu"), follow=True)

        self.assertEqual(
            response.redirect_chain[0][0], "/accounts/login/?next=/generate_files/menu"
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)

    def test_displaying_data_when_logged_in_without_userdata(self):
        self.client.login(username="username", password="password")
        response = self.client.get(reverse("generate_files:menu"), follow=True)

        self.assertEqual(
            response.redirect_chain[0][0], "/your_health/add_data",
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["PATH_INFO"], reverse("your_health:add_data"))

    def test_displaying_data_when_logged_in_with_userdata(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.get(reverse("generate_files:menu"), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["PATH_INFO"], reverse("generate_files:menu"))


class GeneratePDFViewTest(CreateUserData, TestCase):
    def setUp(self):
        self.user = self.create_user()

        self.client = Client()

    def test_redirect_when_logged_out(self):
        response = self.client.get(reverse("generate_files:generate_pdf"), follow=True)

        self.assertEqual(
            response.redirect_chain[0][0],
            "/accounts/login/?next=/generate_files/generate_pdf",
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)

    def test_displaying_data_when_logged_in_without_userdata(self):
        self.client.login(username="username", password="password")
        response = self.client.get(reverse("generate_files:generate_pdf"), follow=True)

        self.assertEqual(
            response.redirect_chain[0][0], "/your_health/add_data",
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["PATH_INFO"], reverse("your_health:add_data"))

    def test_displaying_data_when_logged_in_with_userdata(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.get(reverse("generate_files:generate_pdf"), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("generate_files:generate_pdf"),
        )


class GenerateCSVViewTest(CreateUserData, TestCase):
    def setUp(self):
        self.user = self.create_user()

        self.client = Client()

    def test_redirect_when_logged_out(self):
        response = self.client.get(reverse("generate_files:generate_csv"), follow=True)

        self.assertEqual(
            response.redirect_chain[0][0],
            "/accounts/login/?next=/generate_files/generate_csv",
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)

    def test_displaying_data_when_logged_in_without_userdata(self):
        self.client.login(username="username", password="password")
        response = self.client.get(reverse("generate_files:generate_csv"), follow=True)

        self.assertEqual(
            response.redirect_chain[0][0], "/your_health/add_data",
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["PATH_INFO"], reverse("your_health:add_data"))

    def test_displaying_data_when_logged_in_with_userdata(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.get(reverse("generate_files:generate_csv"), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("generate_files:generate_csv")
        )

    def test_generating_csv_file(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        measurement = self.create_measurement(userdata)
        response = self.client.get(reverse("generate_files:generate_csv"), follow=True)

        content = response.content.decode("utf-8")
        cvs_reader = csv.reader(io.StringIO(content))
        body = list(cvs_reader)
        headers = body.pop(0)
        headers += body.pop(0)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("generate_files:generate_csv")
        )
        self.assertContains(response, "Lp.")
        self.assertContains(response, "Ciśnienie skurczowe")
        self.assertContains(response, "Ciśnienie rozkurczowe")
        self.assertContains(response, "Tętno")
        self.assertContains(response, "Data pomiaru")
        self.assertContains(response, 120)
        self.assertContains(response, 80)
        self.assertContains(response, 60)
