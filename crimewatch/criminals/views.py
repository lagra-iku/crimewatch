from django.shortcuts import render, get_object_or_404, redirect
from .models import Criminal
from .forms import CriminalForm

# Create a criminal
def criminal_create(request):
    if request.method == 'POST':
        form = CriminalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('criminal_list')
    else:
        form = CriminalForm()
    return render(request, 'criminal_form.html', {'form': form})

# Read (list) criminals
def criminal_list(request):
    criminals = Criminal.objects.all()
    return render(request, 'criminal_list.html', {'criminals': criminals})

# Update a criminal
def criminal_update(request, pk):
    criminal = get_object_or_404(Criminal, pk=pk)
    if request.method == 'POST':
        form = CriminalForm(request.POST, instance=criminal)
        if form.is_valid():
            form.save()
            return redirect('criminal_list')
    else:
        form = CriminalForm(instance=criminal)
    return render(request, 'criminal_form.html', {'form': form})

# Delete a criminal
def criminal_delete(request, pk):
    criminal = get_object_or_404(Criminal, pk=pk)
    if request.method == 'POST':
        criminal.delete()
        return redirect('criminal_list')
    return render(request, 'criminal__delete.html', {'criminal': criminal})