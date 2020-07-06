from django.urls import path

from . import views


app_name = 'measurements'

urlpatterns = [
    path('add_measurement', views.MeasurementCreate.as_view(), name='add_measurement'),
]
