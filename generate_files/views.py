from django.shortcuts import render
from django.views.generic.base import TemplateView
from easy_pdf.views import PDFTemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from your_health.mixins import UserDataRequiredMixin

from measurements.models import Measurement


class GenerateFilesMenuView(LoginRequiredMixin, UserDataRequiredMixin, TemplateView):
    template_name = "generate_files/menu.html"


class GeneratePDFView(LoginRequiredMixin, UserDataRequiredMixin, PDFTemplateView):
    """ generates PDF file for each user """

    template_name = "generate_files/PDF_template.html"

    def get_context_data(self, **kwargs):
        measurements = Measurement.queryset_for_user(self, self.request.user)
        print(measurements)

        return super(GeneratePDFView, self).get_context_data(
            pagesize="A4", measurements=measurements
        )


class GenerateCSVView(LoginRequiredMixin, UserDataRequiredMixin, TemplateView):
    template_name = "generate_files/menu.html"
