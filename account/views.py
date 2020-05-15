from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

# Create your views here.


def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Email or Password is incorrect')
    context = {}
    return render(request, 'account/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home_page(request):
    context = {}
    return render(request, 'account/home.html', context)
