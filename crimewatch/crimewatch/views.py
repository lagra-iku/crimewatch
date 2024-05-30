from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from officers.models import Officer
from cases.models import CriminalCase
from criminals.models import CriminalRecord
from django.db.models import Q
from criminals.forms import LogInForm

# Create a new criminal case
@login_required
def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LogInForm()
    return render(request, 'form.html', {'form': form, 'title': 'Login'})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    user = request.user
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'rank': user.policeofficers.rank if hasattr(user, 'policeofficers') else 'N/A',
    }
    return render(request, 'profile.html', context)