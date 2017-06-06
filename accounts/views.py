from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.shortcuts import render

from accounts.forms import UserRegisterForm, UserLogin
from accounts.models import UserProfile, Vendor


def user_register(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html', {'register': False, 'register_form': UserRegisterForm()})

    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data.get('username'),
                first_name=form.cleaned_data.get('firstname'),
                last_name=form.cleaned_data.get('lastname'),
                email=form.cleaned_data.get('email'),
            )

            user.set_password(form.cleaned_data.get('password'))

            user.save()

            if 'type' in request.POST:
                user_profile = Vendor(user=user)
            else:
                user_profile = UserProfile(user=user)

            user_profile.save()

            return render(request, 'accounts/register.html', {'register': True, 'register_form': form})
        else:
            return render(request, 'accounts/register.html', {'register': False, 'register_form': form})


def user_login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'login_form': UserLogin()})

    elif request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            #TODO should redirect to the last page user was in
            return render(request, 'simgun/index.html', {})
        else:
            return render(request, 'accounts/login.html', {'login_form': form})


def user_logout(request):
    logout(request)
    return render(request, 'simgun/index.html', {})