from django.shortcuts import render, redirect
from .forms import PoliceOfficersForm, AddNewOfficerForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout
from datetime import datetime
import bcrypt
from .models import AddNewOfficer
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def app(request):
    return render(request, 'pages/dashboard.html')

def whistledown(request):
    return render(request, 'ladywhistledown.html')


from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Login the authenticated user
                auth_login(request, user)
                return redirect('app')
            else:
                print('Invalid username or password')
                return render(request, 'login.html', {'error_message': 'Invalid username or password'})
        except AddNewOfficer.DoesNotExist:
            print('Username or password invalid')
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    

def logout_view(request):
    logout(request)
    return redirect('login')

def register_officers(request):
    if request.method == 'POST':
        form = AddNewOfficerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages/dashboard.html')
    else:
        form = AddNewOfficerForm()
    return render(request, 'register_officers.html', {'form': form})


def add_new_officer(request):
    if request.method == 'POST':
        form = AddNewOfficerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_new_officer') 
    else:
        form = AddNewOfficerForm()
    return render(request, 'add_new_officer.html', {'form': form})
