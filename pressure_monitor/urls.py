"""pressure_monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    # allauth
    path("accounts/", include("allauth.urls")),
    # custom blood_pressure_monitor urls
    # homepage app
    path("", include("homepage.urls")),
    # your_health app
    path("your_health/", include("your_health.urls")),
    # measurements app
    path("measurements/", include("measurements.urls")),
    # generate_files app
    path("generate_files/", include("generate_files.urls")),
]
