# Create your views here.
from django.shortcuts import render
from django.views import generic

from ketabkhor.forms import UserRegisterForm, UserLogin
from ketabkhor.models import Book, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home_page(request):
    return render(request, "ketabkhor/index.html")


class BookDetails(generic.DetailView):
    model = Book
    template_name = "ketabkhor/book-detail.html"


def user_register(request):
    if request.method == 'GET':
        return render(request, 'ketabkhor/register.html', {'register': False, 'register_form': UserRegisterForm()})

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

            user_profile = UserProfile(
                user=user,
                birthday=form.cleaned_data.get('birthday')
            )

            user_profile.save()

            return render(request, 'ketabkhor/register.html', {'register': True, 'register_form': form})
        else:
            return render(request, 'ketabkhor/register.html', {'register': False, 'register_form': form})


def user_login(request):
    if request.method == 'GET':
        return render(request, 'ketabkhor/login.html', {'login_form': UserLogin()})

    elif request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            #TODO should redirect to the last page user was in
            return render(request, 'ketabkhor/index.html', {})
        else:
            return render(request, 'ketabkhor/login.html', {'login_form': form})