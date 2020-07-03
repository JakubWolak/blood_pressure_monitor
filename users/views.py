from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

from django.http import HttpResponse


def users_login(request, template_name='users/login.html'):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username = cleaned_data['username'], password = cleaned_data['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)

                    # TODO: redirect to main page of the app!!!!
                    return HttpResponse("zalogowano!")
                else:
                    # TODO: redirect to page with error info or add error message to form
                    return HttpResponse('konto zablokowane!')
            else:
                # TODO: add error message to form
                return HttpResponse('nieprawidłowe dane!')
        else:
            form = LoginForm()

    context = {
        'form': form,
    }
    
    return render(request, template_name, context)