from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def app(request):
  template = loader.get_template('pages/dashboard.html')
  return HttpResponse(template.render())
