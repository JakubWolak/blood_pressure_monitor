from django.urls import path

from . import views

app_name = 'your_health'


urlpatterns = [
    path('add_data', views.add_userdata, name='add_data'),
    path('edit_data', views.edit_userdata, name='edit_data'),
]
