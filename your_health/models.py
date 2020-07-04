from django.db import models
from django.conf import settings

from .validators import min_height, max_height, min_weight, max_weight

class UserData(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    name = models.CharField(max_length=50, null=False, blank=False)
    surname =  models.CharField(max_length=50, null=False, blank=False)

    sex = models.CharField(max_length=10, blank=False, null=False)
    height = models.IntegerField(validators=[min_height, max_height], null=False, blank=False)
    weight = models.IntegerField(validators=[min_weight, max_weight], null=False, blank=False)

    def get_full_name(self):
        return '{name} {surname}'.format(name=self.name, surname=self.surname)

    def __str__(self):
        return 'Użytkownik {fullname}, płeć {sex}, wzrost {height}, waga {weight}'.format(
            fullname=self.get_full_name(),
            sex=self.sex,
            height=self.height,
            weight=self.weight
        )
    
