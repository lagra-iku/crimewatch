from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date
from officers.models import Officer
from cases.models import CriminalCase
from criminals.models import CriminalRecord
from django.db.models import Q
from criminals.forms import LogInForm


# Create a new criminal case
@login_required
def home(request):
    officers_on_duty = Officer.objects.filter(duty_status="On Duty")

    # Counts for cases
    open_cases_count = CriminalCase.objects.filter(case_status='active').count()
    closed_cases_count = CriminalCase.objects.filter(case_status='closed').count()

    # Counts for criminals
    female_criminals_count = CriminalRecord.objects.filter(gender='female').count()
    male_criminals_count = CriminalRecord.objects.filter(gender='male').count()

    #Get today's cases
    today = date.today()
    today_cases = CriminalCase.objects.filter(event_date=today)

    context = {
        'officers_on_duty': officers_on_duty,
        'open_cases_count': open_cases_count,
        'closed_cases_count': closed_cases_count,
        'female_criminals_count': female_criminals_count,
        'male_criminals_count': male_criminals_count,
        'today_cases' :  today_cases,
    }
    return render(request, 'home.html', context)


# def login(request):
#     if request.method == 'POST':
#         form = LogInForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 form.add_error(None, 'Invalid username or password')
#     else:
#         form = LogInForm()
#     return render(request, 'login.html', {'form': form, 'title': 'Login'})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    user = request.user
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'rank': user.policeofficers.rank if hasattr(user, 'policeofficers') else 'N/A',
    }
    return render(request, 'profile.html', context)

def search_results(request):
    query = request.GET.get('q')
    criminals = CriminalRecord.objects.filter(
        Q(first_name__icontains=query) |
        Q(surname__icontains=query) |
        Q(known_aliases__icontains=query)
    )
    cases = CriminalCase.objects.filter(
        Q(case_number__icontains=query) |
        Q(case_description__icontains=query)
    )
    context = {
        'query': query,
        'criminals': criminals,
        'cases': cases,
    }
    return render(request, 'search_results.html', context)