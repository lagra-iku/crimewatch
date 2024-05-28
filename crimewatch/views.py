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

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Retrieve the user based on the username
            user = AddNewOfficer.objects.get(username=username)
        except AddNewOfficer.DoesNotExist:
            # Handle case when user does not exist
            return render(request, 'login.html', {'error_message': 'User does not exist'})
        
        if check_password(password, user.password):
            # Log the user in and create a session
            auth_login(request, user)
            return redirect('pages\dashboard')
        else:
            # Authentication failed, handle accordingly (e.g., show an error message)
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

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
