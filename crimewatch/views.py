from django.shortcuts import render, redirect
from .forms import PoliceOfficersForm, AddNewOfficerForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
import bcrypt
from .models import AddNewOfficer
from django.contrib import messages

def app(request):
    return render(request, 'pages/dashboard.html')

def whistledown(request):
    return render(request, 'ladywhistledown.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                officer = AddNewOfficer.objects.get(username=username)
            except AddNewOfficer.DoesNotExist:
                messages.error(request, 'Invalid username or password.')
                return render(request, 'login.html', {'form': form})

            if bcrypt.checkpw(password.encode('utf-8'), officer.password.encode('utf-8')):
                # Authenticate the user
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('app')
                else:
                    messages.error(request, 'Invalid username or password.')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def register_officers(request):
    if request.method == 'POST':
        form = AddNewOfficerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_officers')
    else:
        form = AddNewOfficerForm()
    return render(request, 'register_officers.html', {'form': form})


def add_new_officer(request):
    if request.method == 'POST':
        form = AddNewOfficerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin') 
    else:
        form = AddNewOfficerForm()
    return render(request, 'add_new_officer.html', {'form': form})
