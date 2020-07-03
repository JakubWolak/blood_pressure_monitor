from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('change_password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(), name='change_password_done'),
]