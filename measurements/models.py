from django.db import models

from your_health.models import UserData
from .validators import *


class Measurement(models.Model):
    userdata = models.ForeignKey(UserData, on_delete=models.PROTECT)

    measurement_time = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Data pomiaru"
    )

    systolic_pressure = models.SmallIntegerField(
        null=False,
        blank=False,
        default=120,
        verbose_name="Ciśnienie skurczowe",
        validators=[max_systolic_pressure, min_systolic_pressure],
    )
    diastolic_pressure = models.SmallIntegerField(
        null=False,
        blank=False,
        default=80,
        verbose_name="Ciśnienie rozkurczowe",
        validators=[max_diastolic_pressure, min_diastolic_pressure],
    )
    pulse = models.SmallIntegerField(
        null=False,
        blank=False,
        default=60,
        verbose_name="Tętno",
        validators=[max_pulse, min_pulse],
    )

    class Meta:
        ordering = ["-measurement_time"]

    def queryset_for_user(self, user):
        """
        takes request.user as an argument and returns all 
        measurements where userdata's foreign key equals given arugment 
        """
        try:
            userdata = UserData.objects.get(user=user)
            queryset = Measurement.objects.filter(userdata=userdata)
        except:
            queryset = {}

        return queryset

    def __str__(self):
        info_message = "Pomiar dla: {user}, wynik: {systolic}/{diastolic}, tętno: {pulse}".format(
            user=self.userdata.get_full_name(),
            systolic=self.systolic_pressure,
            diastolic=self.diastolic_pressure,
            pulse=self.pulse,
        )
        return info_message

