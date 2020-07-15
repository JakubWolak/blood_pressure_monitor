from django.urls import path

from .views import *


app_name = "generate_files"

url_patterns = [
    path("menu", views.GenerateFilesMenuView.as_view(), "menu"),
]
