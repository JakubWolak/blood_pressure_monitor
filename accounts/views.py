from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

from django.http import HttpResponse


def register(request, template_name='registration/register.html'):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            print('valid form')
            form.save()

            return(redirect(reverse('accounts:login')))
        # TODO: redirect to home page
    else:
        form = RegisterForm()

    context = {
        'form': form,
        }
    
    return render(request, template_name, context)