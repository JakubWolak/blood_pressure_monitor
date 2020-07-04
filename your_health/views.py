from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .decorators import userdata_exists
from .forms import UserDataForm
from .models import UserData


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


@login_required
@userdata_exists
def edit_userdata(request, template_name='your_health/add_userdata.html'):
    """
    edits existing userdata
    """
    userdata = get_object_or_404(UserData, user=request.user)

    if request.method == 'POST':
        form = UserDataForm(request.POST, instance=userdata)

        if form.is_valid():
            form.save()

            return redirect(reverse('homepage:index'))
    else:
        form = UserDataForm(instance=userdata)

    context = {
        'form': form
    }

    return render(request, template_name, context)