from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import RegistrationUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def registrationView(request):
    if request.method == 'POST':
        form = RegistrationUserForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')
            firstname = cleaned_data.get('nombre')
            lastname = cleaned_data.get('apellido')

            user_model = User.objects.create_user(username=username, password=password, email=email,
                                                  firstname=firstname, lastname=lastname)
            user_model.save()
            return redirect(reverse('accounts.profile', {'username': username}))
    else:
        form = RegistrationUserForm()
    return render(request, 'accounts/registration.html', {'form': form})


@login_required

def profile(request):
    return render(request, 'accounts/profile.html')


def loginView(request):

    if request.user.is_authenticated():
        return redirect(reverse('accounts.profile'))


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('accounts.profile'))
            else:
                return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')


def logoutView(request):
    logout(request)
    return redirect(reverse('accounts.login'))