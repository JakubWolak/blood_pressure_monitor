from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def min_systolic_pressure(pressure):
    min_systolic = 70

    if pressure < min_systolic:
        raise ValidationError(_('Minimalne ciśnienie skurczowe to {0}mm Hg!'.format(min_systolic)))


def max_systolic_pressure(pressure):
    max_systolic = 250

    if pressure > max_systolic:
        raise ValidationError(_('Maksymalne ciśnienie skurczowe to {0}mm Hg!'.format(max_systolic)))


def min_diastolic_pressure(pressure):
    min_diastolic = 20

    if pressure < min_diastolic:
        raise ValidationError(_('Minimalne ciśnienie skurczowe to {0}mm Hg!'.format(min_diastolic)))


def max_diastolic_pressure(pressure):
    max_diastolic = 180

    if pressure > max_diastolic:
        raise ValidationError(_('Maksymalne ciśnienie skurczowe to {0}mm Hg!'.format(max_diastolic)))


def min_pulse(pulse):
    min_pulse = 15

    if pulse < min_pulse:
        raise ValidationError(_('Minimalne tętno to {0} uderzeń / min !'.format(min_pulse)))


def max_pulse(pulse):
    max_pulse = 200

    if pulse > max_pulse:
        raise ValidationError(_('Maksymalne tętno to {0} uderzeń / min !'.format(max_pulse)))