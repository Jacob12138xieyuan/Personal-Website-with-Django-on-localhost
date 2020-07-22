from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm

# Create your views here.


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homePage')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'loginPage.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        registerForm = RegisterUserForm()

        if request.method == 'POST':
            registerForm = RegisterUserForm(request.POST)
            if registerForm.is_valid():
                registerForm.save()
                username = registerForm.cleaned_data.get('username')
                messages.success(request, 'Account is created for '+username)
                return redirect('loginPage')

        context = {'registerForm': registerForm}
        return render(request, 'registerPage.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')
