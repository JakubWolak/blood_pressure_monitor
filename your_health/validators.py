from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def min_height(height):
    min_height = 50

    if height < min_height:
        raise ValidationError(_('Minimalny wzrost to {0} cm!'.format(min_height)))


def max_height(height):
    max_height = 230

    if height > max_height:
        raise ValidationError(_('Maksymalny wzrost to {0} cm!'.format(max_height)))


def min_weight(weight):
    min_weight = 20

    if weight < min_weight:
        raise ValidationError(_('Minimalna waga to {0} kg!'.format(max_weight)))


def max_weight(weight):
    max_weight = 300

    if weight > max_weight:
        raise ValidationError(_('Maksymalna waga to {0} kg!'.format(max_weight)))