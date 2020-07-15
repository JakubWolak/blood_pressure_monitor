from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from your_health.mixins import UserDataRequiredMixin


class GenerateFilesMenuView(LoginRequiredMixin, UserDataRequiredMixin, TemplateView):
    template_name = "generate_files/menu.html"
