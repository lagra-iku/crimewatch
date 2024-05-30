from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from officers.models import Officer
from cases.models import CriminalCase
from criminals.models import CriminalRecord
from django.db.models import Q

# Create a new criminal case
def home(request):
    return render(request, 'home.html')