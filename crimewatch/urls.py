"""
URL configuration for crimewatch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import whistledown, login, register_officers, logout_view, add_new_officer, create_criminal_record
urlpatterns = [
    path('', include('app.urls')),  # Assuming you have an app named 'app' with its own urls.py
    path('admin/', admin.site.urls),
    path('whistledown/', whistledown, name='whistledown'),
    path('login/', login, name='login'),
    path('register_officers/', register_officers, name='register_officers'),
    path('logout/', logout_view, name='logout'),
    path('add_new_officer/', add_new_officer, name='add_new_officer'),
    path('create_criminal_record/', create_criminal_record, name='create_criminal_record'),
]