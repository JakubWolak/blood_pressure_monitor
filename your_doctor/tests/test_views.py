from django.test import TestCase, Client

from django.shortcuts import reverse

from django.contrib.auth.models import User
from your_health.models import UserData


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
    def create_userdata(self):
        userdata = Userdata.objects.create()

    class Meta:
        abstract = True


class DoctorDataCreateViewTest(CreateUserData, TestCase):
    def setUp(self):
        self.user = self.create_user()

        self.client = Client()

    def test_redirect_when_logged_out(self):
        response = self.client.get(reverse("your_doctor:add_data"), follow=True)

        self.assertEqual(
            response.redirect_chain[0][0], "accounts/login/?next=/your_doctor/add_data"
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)

    def test_context_data_when_logged_in_with_userdata(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.get(reverse("your_doctor:add_data"), follow=True)

        self.assertEqual(response.context["user"], userdata)

    def test_context_data_when_logged_in_with_userdata(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.get(reverse("your_doctor:edit_data"), follow=True)

        self.assertEqual(response.context["user"], userdata)

    def test_displaying_view_when_logged_in_with_userdata(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.get(reverse("your_doctor:edit_data"), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("your_doctor:edit_data")
        )

    def test_view_when_invalid_data_given(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.post(
            reverse("your_doctor:add_data"),
            {"name": 12341234, "surname": 2343, "email": "email@email.com"},
            follow=True,
        )
        messages = list(response.context["messages"])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["PATH_INFO"], reverse("your_doctor:add_data"))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Niepoprawnie wypełniony formularz")

    def test_name_required(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.post(
            reverse("your_doctor:add_data"),
            {"surname": "surname", "email": "email@email.com"},
            follow=True,
        )

        self.assertFormError(response, "form", "name", "This field is required.")

    def test_surname_required(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.post(
            reverse("your_doctor:add_data"),
            {"name": "name", "email": "email@email.com"},
            follow=True,
        )

        self.assertFormError(response, "form", "surname", "This field is required.")

    def test_email_required(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.post(
            reverse("your_doctor:add_data"),
            {"name": "name", "surname": "surname"},
            follow=True,
        )

        self.assertFormError(response, "form", "email", "This field is required.")

    def test_saving_userdata_when_valid_data_given(self):
        self.client.login(username="username", password="password")
        response = self.client.post(
            reverse("your_doctor:add_data"),
            {"name": "name", "surname": "surname", "email": "email@email.com",},
            follow=True,
        )
        messages = list(response.context["messages"])

        user = UserData.objects.get(user=self.user)
        doctor = DoctorData.objects.get(userdata=user)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0][0], reverse("homepage:index"))
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertTrue(doctor)
        self.assertEqual(doctor.name, "name")
        self.assertEqual(doctor.surname, "surname")
        self.assertEqual(doctor.email, "email@email.com")
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Pomyślnie zaktualizowano dane lekarza")


class DoctorDataUpdateViewTest(CreateUserData, TestCase):
    def setUp(self):
        self.user = self.create_user()

        self.client = Client()

    def test_redirect_when_logged_out(self):
        response = self.client.get(reverse("your_doctor:edit_data"), follow=True)

        self.assertEqual(
            response.redirect_chain[0][0],
            "/accounts/login/?next=/your_doctor/edit_data",
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)

    def test_context_data_when_logged_in_with_userdata(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.get(reverse("your_doctor:edit_data"), follow=True)

        self.assertEqual(response.context["user"], userdata)

    def test_displaying_view_when_logged_in_with_userdata(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.get(reverse("your_doctor:edit_data"), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("your_doctor:edit_data")
        )

    def test_redirect_and_messages_when_logged_in_without_userdata(self):
        self.client.login(username="username", password="password")
        response = self.client.get(reverse("your_doctor:edit_data"), follow=True)
        userdata = self.create_userdata(self.user)
        messages = list(response.context["messages"])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["PATH_INFO"], reverse("your_doctor:add_data"))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Uzupełnij swoje dane")

    def test_view_when_invalid_data_given(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.post(
            reverse("your_doctor:edit_data"),
            {"name": "sss", "surname": 123123,},
            follow=True,
        )
        messages = list(response.context["messages"])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("your_doctor:edit_data")
        )
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Niepoprawnie wypełniony formularz")

    def test_view_when_valid_data_given(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.post(
            reverse("your_doctor:edit_data"),
            {"name": "name1", "surname": "surname1", "email": "email@email1.com",},
            follow=True,
        )
        messages = list(response.context["messages"])

        userdata = UserData.objects.get(user=self.user)
        doctor = DoctorData.objects.get(userdat=userdata)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0][0], reverse("homepage:index"))
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertTrue(doctor)
        self.assertEqual(doctor.name, "name1")
        self.assertEqual(doctor.surname, "surname1")
        self.assertEqual(doctor.sex, "email@email1.com")
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Pomyślnie zaktualizowano dane lekarza")
