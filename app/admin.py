from django.contrib import admin
from .models import PoliceOfficers, AddNewOfficer, CriminalRecord
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin import AdminSite

# Register your models here.



admin.site.site_header = "CrimeWatch Administration"
admin.site.site_title = "CrimeWatch Administration Portal"
admin.site.index_title = "Welcome to the CrimeWatch Administration Dashboard"

admin.site.register(PoliceOfficers)
admin.site.register(AddNewOfficer)

