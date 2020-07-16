from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from easy_pdf.views import PDFTemplateView
import csv
from django.http import HttpResponse

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


class GenerateCSVView(LoginRequiredMixin, UserDataRequiredMixin, View):
    """ generates CSV file for each user """

    def get(self, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="tabela_pomiarow.csv"'

        writer = csv.writer(response, delimiter="|")
        writer.writerow(["Tabela pomiarów ciśnienia krwi"])
        writer.writerow(
            [
                "Lp.",
                "Ciśnienie skurczowe",
                "Ciśnienie rozkurczowe",
                "Tętno",
                "Data pomiaru",
            ]
        )

        for id, measurement in enumerate(
            Measurement.queryset_for_user(self, self.request.user), 1
        ):
            row = [
                id,
                measurement.systolic_pressure,
                measurement.diastolic_pressure,
                measurement.pulse,
                measurement.measurement_time.strftime("%H:%M  %d %b %Y"),
            ]
            writer.writerow(row)

        return response
