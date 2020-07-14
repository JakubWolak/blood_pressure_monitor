from django.test import TestCase, Client

from django.contrib.auth.models import User
from your_health.models import UserData
from your_health.views import UserDataCreateView, UserDataUpdateView
from django.shortcuts import reverse


class UserDataCreateViewTest(TestCase):
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

        self.client = Client()

    def test_redirect_when_logged_out(self):
        response = self.client.get(reverse("your_health:add_data"), follow=True)

        self.assertEqual(
            response.redirect_chain[0][0], "/accounts/login/?next=/your_health/add_data"
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)

    def test_displaying_view_when_logged_in(self):
        self.client.login(username="username", password="password")
        response = self.client.get(reverse("your_health:add_data"), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["PATH_INFO"], reverse("your_health:add_data"))

    def test_view_when_invalid_data_given(self):
        self.client.login(username="username", password="password")
        response = self.client.post(
            reverse("your_health:add_data"),
            {"height": 190, "weight": 90,},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["PATH_INFO"], reverse("your_health:add_data"))

    def test_name_required(self):
        self.client.login(username="username", password="password")
        response = self.client.post(
            reverse("your_health:add_data"),
            {"surname": "surname", "sex": "male", "height": 190, "weight": 90,},
            follow=True,
        )

        self.assertFormError(response, "form", "name", "This field is required.")

    def test_surname_required(self):
        self.client.login(username="username", password="password")
        response = self.client.post(
            reverse("your_health:add_data"),
            {"name": "name", "sex": "male", "height": 190, "weight": 90,},
            follow=True,
        )

        self.assertFormError(response, "form", "surname", "This field is required.")

    def test_sex_required(self):
        self.client.login(username="username", password="password")
        response = self.client.post(
            reverse("your_health:add_data"),
            {"name": "name", "surname": "surname", "height": 190, "weight": 90,},
            follow=True,
        )

        self.assertFormError(response, "form", "sex", "This field is required.")

    def test_height_required(self):
        self.client.login(username="username", password="password")
        response = self.client.post(
            reverse("your_health:add_data"),
            {"name": "name", "surname": "surname", "sex": "male", "weight": 90,},
            follow=True,
        )

        self.assertFormError(response, "form", "height", "This field is required.")

    def test_weight_required(self):
        self.client.login(username="username", password="password")
        response = self.client.post(
            reverse("your_health:add_data"),
            {"name": "name", "surname": "surname", "sex": "male", "height": 190},
            follow=True,
        )

        self.assertFormError(response, "form", "weight", "This field is required.")

    def test_saving_userdata_when_valid_data_given(self):
        self.client.login(username="username", password="password")
        response = self.client.post(
            reverse("your_health:add_data"),
            {
                "name": "name",
                "surname": "surname",
                "sex": "male",
                "height": 190,
                "weight": 90,
            },
            follow=True,
        )
        messages = list(response.context["messages"])

        user = UserData.objects.get(user=self.user)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0][0], reverse("homepage:index"))
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertTrue(user)
        self.assertEqual(user.name, "name")
        self.assertEqual(user.surname, "surname")
        self.assertEqual(user.sex, "male")
        self.assertEqual(user.height, 190)
        self.assertEqual(user.weight, 90)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Pomyślnie zaktualizowano dane")


class UserDataUpdateView(TestCase):
    @classmethod
    def create_userdata(self, user):
        userdata = UserData.objects.create(
            user=user,
            name="first_name",
            surname="last_name",
            sex="male",
            height=190,
            weight=90,
        )
        return userdata

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

        self.client = Client()

    def test_redirect_when_logged_out(self):
        response = self.client.get(reverse("your_health:edit_data"), follow=True)

        self.assertEqual(
            response.redirect_chain[0][0],
            "/accounts/login/?next=/your_health/edit_data",
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)

    def test_context_data_when_logged_in_with_userdata(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.get(reverse("your_health:edit_data"), follow=True)

        self.assertEqual(response.context["user"], userdata)

    def test_displaying_view_when_logged_in_with_userdata(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.get(reverse("your_health:edit_data"), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("your_health:edit_data")
        )

    def test_redirect_and_messages_when_logged_in_without_userdata(self):
        self.client.login(username="username", password="password")
        response = self.client.get(reverse("your_health:edit_data"), follow=True)
        messages = list(response.context["messages"])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["PATH_INFO"], reverse("your_health:add_data"))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Uzupełnij swoje dane")

    def test_view_when_invalid_data_given(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.post(
            reverse("your_health:edit_data"),
            {"sex": "sss", "weight": "weight",},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"], reverse("your_health:edit_data")
        )

    def test_view_when_valid_data_given(self):
        self.client.login(username="username", password="password")
        userdata = self.create_userdata(self.user)
        response = self.client.post(
            reverse("your_health:edit_data"),
            {
                "name": "name1",
                "surname": "surname1",
                "sex": "female",
                "height": 191,
                "weight": 91,
            },
            follow=True,
        )
        messages = list(response.context["messages"])

        userdata = UserData.objects.get(user=self.user)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0][0], reverse("homepage:index"))
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertTrue(userdata)
        self.assertEqual(userdata.name, "name1")
        self.assertEqual(userdata.surname, "surname1")
        self.assertEqual(userdata.sex, "female")
        self.assertEqual(userdata.height, 191)
        self.assertEqual(userdata.weight, 91)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Pomyślnie zaktualizowano dane")

