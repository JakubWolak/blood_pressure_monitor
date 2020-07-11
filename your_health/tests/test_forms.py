from django.test import TestCase

from your_health.forms import UserDataForm


class UserDataFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "name": "name",
            "surname": "surname",
            "sex": "male",
            "height": 190,
            "weight": 90,
        }
        form = UserDataForm(form_data)

        self.assertTrue(form.is_valid())

    def test_surname_required(self):
        form_data = {
            "name": "name",
            "sex": "male",
            "height": 190,
            "weight": 90,
        }
        form = UserDataForm(form_data)

        self.assertFalse(form.is_valid())

    def test_sex_required(self):
        form_data = {
            "name": "name",
            "surname": "surname",
            "height": 190,
            "weight": 90,
        }
        form = UserDataForm(form_data)

        self.assertFalse(form.is_valid())

    def test_height_required(self):
        form_data = {
            "name": "name",
            "surname": "surname",
            "sex": "male",
            "weight": 90,
        }
        form = UserDataForm(form_data)

        self.assertFalse(form.is_valid())

    def test_weight_required(self):
        form_data = {
            "name": "name",
            "surname": "surname",
            "sex": "male",
            "height": 190,
        }
        form = UserDataForm(form_data)

        self.assertFalse(form.is_valid())
