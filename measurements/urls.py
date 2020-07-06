from django.urls import path

from . import views


app_name = 'measurements'

urlpatterns = [
    # adding a new measurement
    path('add_measurement', views.MeasurementCreate.as_view(), name='add_measurement'),

    # showing all measurements
    path('show_measurements', views.MeasurementListView.as_view(), name='show_measurements'),
]
