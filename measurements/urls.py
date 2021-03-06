from django.urls import path

from . import views


app_name = "measurements"

urlpatterns = [
    # adding a new measurement
    path(
        "add_measurement", views.MeasurementCreateView.as_view(), name="add_measurement"
    ),
    # showing all measurements
    path(
        "show_measurements",
        views.MeasurementTableView.as_view(),
        name="show_measurements",
    ),
]
