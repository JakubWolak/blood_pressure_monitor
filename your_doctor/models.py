from django.db import models

from your_health.models import UserData


class DoctorData(models.Model):
    """ class to store data about user's doctor """

    userdata = models.ForeignKey(UserData, on_delete=models.PROTECT)

    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Imię")
    surname = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Nazwisko"
    )

    email = models.EmailField(
        null=False, blank=False, max_length=100, verbose_name="Email"
    )

    def __str__(self):
        return "Kardiolog {name} {surname}".format(name=self.name, surname=self.surname)

    def get_full_name(self):
        return "{name} {surname}".format(name=self.name, surname=self.surname)

