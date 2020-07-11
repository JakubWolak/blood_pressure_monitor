from django.test import SimpleTestCase

from measurements.validators import *


class ValidatorsTest(SimpleTestCase):
    def test_min_systolic_pressure(self):
        lower_value = 69
        valid_value = 70
        higher_value = 71

        self.assertRaises(ValidationError, min_systolic_pressure, lower_value)
        self.assertIsNone(min_systolic_pressure(valid_value))
        self.assertIsNone(min_systolic_pressure(higher_value))

    def test_max_systolic_pressure(self):
        lower_value = 249
        valid_value = 250
        higher_value = 251

        self.assertRaises(ValidationError, max_systolic_pressure, higher_value)
        self.assertIsNone(max_systolic_pressure(valid_value))
        self.assertIsNone(max_systolic_pressure(lower_value))

    def test_min_diastolic_pressure(self):
        lower_value = 19
        valid_value = 20
        higher_value = 21

        self.assertRaises(ValidationError, min_diastolic_pressure, lower_value)
        self.assertIsNone(min_diastolic_pressure(valid_value))
        self.assertIsNone(min_diastolic_pressure(higher_value))

    def test_max_diastolic_pressure(self):
        lower_value = 179
        valid_value = 180
        higher_value = 181

        self.assertRaises(ValidationError, max_diastolic_pressure, higher_value)
        self.assertIsNone(max_diastolic_pressure(valid_value))
        self.assertIsNone(max_diastolic_pressure(lower_value))

    def test_min_pulse(self):
        lower_value = 14
        valid_value = 15
        higher_value = 16

        self.assertRaises(ValidationError, min_pulse, lower_value)
        self.assertIsNone(min_pulse(valid_value))
        self.assertIsNone(min_pulse(higher_value))

    def test_max_pulse(self):
        lower_value = 199
        valid_value = 200
        higher_value = 201

        self.assertRaises(ValidationError, max_pulse, higher_value)
        self.assertIsNone(max_pulse(valid_value))
        self.assertIsNone(max_pulse(lower_value))
