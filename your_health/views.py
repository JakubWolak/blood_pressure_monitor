from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import UserDataForm


@login_required
def add_userdata(request, template_name='your_health/add_userdata.html'):
    """
    creates new userdata
    """

    if request.method == 'POST':
        form = UserDataForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            return redirect(reverse('homepage:index'))
        
    else:
        form = UserDataForm()
        
    context = {
        'form': form
    }
        
    return render(request, template_name, context)