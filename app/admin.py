from django.contrib import admin
from .models import PoliceOfficers, AddNewOfficer, CriminalRecord

admin.site.site_header = "CrimeWatch Administration"
admin.site.site_title = "CrimeWatch Administration Portal"
admin.site.index_title = "Welcome to the CrimeWatch Administration Dashboard"

admin.site.register(PoliceOfficers)

@admin.register(AddNewOfficer)
class AddNewOfficerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'surname', 'rank', 'password','username', 'badge_number', 'status')
    search_fields = ('first_name', 'surname', 'username', 'badge_number')
    list_filter = ('rank', 'status')

admin.site.register(CriminalRecord)
