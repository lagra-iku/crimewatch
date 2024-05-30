from django.http import HttpResponse
from django.shortcuts import render
from officers.models import Officer
from cases.models import CriminalCase
from criminals.models import CriminalRecord
from django.db.models import Q

# Create a new criminal case
def home(request):
    officers_on_duty = Officer.objects.filter(duty_status="On Duty")

    # Counts for cases
    open_cases_count = CriminalCase.objects.filter(case_status='active').count()
    closed_cases_count = CriminalCase.objects.filter(case_status='closed').count()
    
    # Counts for criminals
    female_criminals_count = CriminalRecord.objects.filter(gender='female').count()
    male_criminals_count = CriminalRecord.objects.filter(gender='male').count()

    context = {
        'officers_on_duty': officers_on_duty,
        'open_cases_count': open_cases_count,
        'closed_cases_count': closed_cases_count,
        'female_criminals_count': female_criminals_count,
        'male_criminals_count': male_criminals_count,
    }
    return render(request, 'home.html', context)

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



