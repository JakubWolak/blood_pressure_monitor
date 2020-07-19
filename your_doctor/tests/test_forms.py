from django.test import TestCase

from your_doctor.forms import DoctorDataForm


class DoctorDataFromTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "name": "name",
            "surname": "surname",
            "email": "email@email.com",
        }
        form = DoctorDataForm(form_data)

        self.assertTrue(form.is_valid())

    def test_name_required(self):
        form_data = {
            "surname": "surname",
            "email": "email@email.com",
        }
        form = DoctorDataForm(form_data)

        self.assertFalse(form.is_valid())

    def test_surname_required(self):
        form_data = {
            "name": "name",
            "email": "email@email.com",
        }
        form = DoctorDataForm(form_data)

        self.assertFalse(form.is_valid())

    def test_email_required(self):
        form_data = {
            "name": "name",
            "surname": "surname",
        }
        form = DoctorDataForm(form_data)

        self.assertFalse(form.is_valid())
