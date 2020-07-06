from django.urls import path

from . import views

app_name = 'your_health'


urlpatterns = [
    path('add_data', views.UserDataCreate.as_view(), name='add_data'),
    path('edit_data', views.UserDataUpdate.as_view(), name='edit_data'),
]
