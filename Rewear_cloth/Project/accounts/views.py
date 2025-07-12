from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserSignupForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import AccountDetail
from .forms import AccountDetailForm

def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')  # landing page
    else:
        form = UserSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')


def profile_view(request):
    profile, created = AccountDetail.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = AccountDetailForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = AccountDetailForm(instance=profile)

    return render(request, 'accounts/profile.html', {'form': form})