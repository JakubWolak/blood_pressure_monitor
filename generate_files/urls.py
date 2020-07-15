from django.urls import path

from . import views


app_name = "generate_files"

urlpatterns = [
    path("menu", views.GenerateFilesMenuView.as_view(), name="menu"),
    path("generate_pdf", views.GeneratePDFView.as_view(), name="generate_pdf"),
    path("generate_csv", views.GenerateCSVView.as_view(), name="generate_csv"),
]
