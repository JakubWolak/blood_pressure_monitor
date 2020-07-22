from django.test import TestCase, Client
from django.urls import reverse_lazy

from django.contrib.auth.models import User


class ViewTestBase(TestCase):
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

    def test_redirect_when_logged_out(self):
        response = self.client.get(
            reverse_lazy("your_health:{view_name}".format(view_name=self.view_name)),
            follow=True,
        )

        self.assertEqual(
            response.redirect_chain[0][0],
            ("/accounts/login/?next=/your_health/" + self.view_name),
        )
        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(response.status_code, 200)

    def test_displaying_view_when_logged_in(self):
        self.client.login(username="username", password="password")
        response = self.client.get(
            reverse_lazy("your_health:{view_name}".format(view_name=self.view_name)),
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.request["PATH_INFO"],
            reverse_lazy("your_health:{view_name}".format(view_name=self.view_name)),
        )

    class Meta:
        abstract = True
