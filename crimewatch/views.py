from django.shortcuts import render, redirect
from .forms import PoliceOfficersForm, AddNewOfficerForm, LoginForms
from django.contrib.auth import authenticate, login
from datetime import datetime
import bcrypt
from .models import AddNewOfficer
from django.contrib.auth import login, logout
from django.contrib import messages

dat = datetime.now()
date = dat.strftime("%Y")

def app(request):
    return render(request, 'dashboard.html')

def whistledown(request):
    return render(request, 'ladywhistledown.html')

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                officer = AddNewOfficer.objects.get(username=username)
            except AddNewOfficer.DoesNotExist:
                messages.error(request, 'Invalid username or password.')
                return render(request, 'login.html', {'form': form})

            if bcrypt.checkpw(password.encode('utf-8'), officer.password.encode('utf-8')):
                # If password matches, set session and redirect
                request.session['officer_id'] = officer.id
                return redirect('whistledown')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForms()
    
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