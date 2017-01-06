# Create your views here.
from django.shortcuts import render
from django.views import generic

from ketabkhor.forms import UserRegisterForm
from ketabkhor.models import Book, UserProfile
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
                password=form.cleaned_data.get('password'),
                first_name=form.cleaned_data.get('firstname'),
                last_name=form.cleaned_data.get('lastname'),
                email=form.cleaned_data.get('email'),
            )

            user.save()

            user_profile = UserProfile(
                user=user,
                birthday=form.cleaned_data.get('birthday')
            )

            user_profile.save()

            return render(request, 'ketabkhor/register.html', {'register': True, 'register_form': form})
        else:
            return render(request, 'ketabkhor/register.html', {'register': False, 'register_form': form})
