from django.urls import path

from . import views


app_name = "your_doctor"

urlpatterns = [
    path("add_data", views.DoctorDataCreateView.as_view(), name="add_data"),
    path("edit_data", views.DoctorDataUpdateView.as_view(), name="edit_data"),
    path("send_data", views.SendDataToDoctorView.as_view(), name="send_data"),
]
