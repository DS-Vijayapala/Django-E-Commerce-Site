""" This file is used to create the views for the User app. """

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    """ This function is used to render the register page. """

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}, your account has been created!')
            form.save()
    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)
