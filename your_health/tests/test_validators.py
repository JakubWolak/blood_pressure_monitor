import unittest
from django.test import SimpleTestCase

from your_health.validators import *
from django.core.exceptions import ValidationError


class ValidatorsTest(SimpleTestCase):
    def test_min_height_validator(self):
        lower_value = 49
        valid_value = 50
        higher_value = 51

        self.assertRaises(ValidationError, min_height, lower_value)
        self.assertIsNone(min_height(valid_value))
        self.assertIsNone(min_height(higher_value))

    def test_max_height_validator(self):
        lower_value = 229
        valid_value = 230
        higher_value = 231

        self.assertRaises(ValidationError, max_height, higher_value)
        self.assertIsNone(max_height(valid_value))
        self.assertIsNone(max_height(lower_value))

    def test_min_weight_value(self):
        lower_value = 19
        valid_value = 20
        higher_value = 21

        self.assertRaises(ValidationError, min_weight, lower_value)
        self.assertIsNone(min_weight(valid_value))
        self.assertIsNone(min_weight(higher_value))

    def test_max_weight_value(self):
        lower_value = 299
        valid_value = 300
        higher_value = 301

        self.assertRaises(ValidationError, max_weight, higher_value)
        self.assertIsNone(max_weight(valid_value))
        self.assertIsNone(max_weight(lower_value))


