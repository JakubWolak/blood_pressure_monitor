from django.urls import path, include
from django.contrib.auth import views
from . import views as app_views

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]