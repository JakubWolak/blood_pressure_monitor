from django.urls import path

from . import views

app_name = "your_health"


urlpatterns = [
    path("add_data", views.UserDataCreateView.as_view(), name="add_data"),
    path("edit_data", views.UserDataUpdateView.as_view(), name="edit_data"),
]
