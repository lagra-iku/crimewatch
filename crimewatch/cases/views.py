from django.shortcuts import render, get_object_or_404, redirect
from .models import CriminalCase
from .forms import CriminalCaseForm

# Create a new criminal case
def case_create(request):
    if request.method == 'POST':
        form = CriminalCaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    else:
        form = CriminalCaseForm()
    return render(request, 'case_form.html', {'form': form})

# List all cases
def case_list(request):
    cases = CriminalCase.objects.all()
    return render(request, 'case_list.html', {'cases': cases})

# Update an existing case
def case_update(request, pk):
    criminal_case = get_object_or_404(CriminalCase, pk=pk)
    if request.method == 'POST':
        form = CriminalCaseForm(request.POST, request.FILES, instance=criminal_case)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    else:
        form = CriminalCaseForm(instance=criminal_case)
    return render(request, 'case_form.html', {'form': form})

# Delete a case
def case_delete(request, pk):
    criminal_case = get_object_or_404(CriminalCase, pk=pk)
    if request.method == 'POST':
        criminal_case.delete()
        return redirect('case_list')
    return render(request, 'case_delete.html', {'case': criminal_case})
