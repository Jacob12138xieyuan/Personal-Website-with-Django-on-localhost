from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .tokens import account_activation_token
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
                user = registerForm.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                email_subject = 'Activate your account'
                message = render_to_string('activateMessage.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid64': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                userEmail = registerForm.cleaned_data.get('email')
                print('uid ' + urlsafe_base64_encode(force_bytes(user.pk)))
                print('token ' + account_activation_token.make_token(user))
                print(message)
                email = EmailMessage(
                    email_subject,
                    message,
                    'xiey0017@gmail.com',
                    to=[userEmail]
                )
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')

        context = {'registerForm': registerForm}
        return render(request, 'registerPage.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


def activate(request, uidb64, token):
    print('activate...')
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account is created for ' + user.username)
        return redirect('loginPage')
    else:
        return HttpResponse('Activation link is invalid!')
