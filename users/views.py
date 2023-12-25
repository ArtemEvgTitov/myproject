from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from .models import Profile
from django.contrib.auth import logout


def logout_user(request):
    logout(request)
    return render(request, 'users/account.html')


def account(request):
    return render(request, 'users/account.html')


def profile(request):
    return render(request, 'users/profile.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'users/profile.html')
                else:
                    return render(request, 'users/login.html', {'form': form})
            else:
                return render(request, 'users/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'users/account.html',
                          {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request,
                  'users/register.html',
                  {'form': form})
