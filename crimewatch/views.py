from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import PoliceOfficersForm

def app(request):
  template = loader.get_template('dashboard.html')
  return HttpResponse(template.render())

def whistledown(request):
    template = loader.get_template('ladywhistledown.html')
    return HttpResponse(template.render())

def loginpage(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def register_officers(request):
    if request.method == 'POST':
        form = PoliceOfficersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_author')
    else:
        form = PoliceOfficersForm()
    return render(request, 'register_officers.html', {'form': form})