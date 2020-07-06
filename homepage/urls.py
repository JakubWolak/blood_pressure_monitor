from django.urls import path

from . import views
from . import api


app_name = 'homepage'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),


    # api path to render charts in the homepage
    path('api/get_data', api.ChartData.as_view(), name='get_api_data'),
]
