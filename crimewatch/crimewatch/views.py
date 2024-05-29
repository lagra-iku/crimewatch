from django.http import HttpResponse
from django.shortcuts import render

# Create a new criminal case
def home(request):
    return render(request, 'home.html')