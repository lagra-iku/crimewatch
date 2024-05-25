from django import forms
from .models import PoliceOfficers, AddNewOfficer


class PoliceOfficersForm(forms.ModelForm):
    """Creates a form for registering police officers"""
    class Meta:
        model = PoliceOfficers
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
        
class AddNewOfficerForm(forms.ModelForm):
    """Creates a new form for adding a new police officer"""
    class Meta:
        model = AddNewOfficer
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }