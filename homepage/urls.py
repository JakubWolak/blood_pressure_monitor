from django.urls import path

from . import views
from . import api


app_name = 'homepage'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('systolic_pressure', views.SystolicPressureView.as_view(), name='systolic_pressure'),
    path('diastolic_pressure', views.DiastolicPressureView.as_view(), name='diastolic_pressure'),
    path('pulse', views.PulseView.as_view(), name='pulse'),


    # api path to render charts in the homepage
    path('api/get_data', api.ChartData.as_view(), name='get_api_data'),
]
