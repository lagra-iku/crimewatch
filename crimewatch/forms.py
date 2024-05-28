from django import forms
from .models import PoliceOfficers, AddNewOfficer, NewCase, CriminalRecord


class PoliceOfficersForm(forms.ModelForm):
    """Creates a form for registering police officers"""
    class Meta:
        model = PoliceOfficers
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class NewCaseForm(forms.ModelForm):
    """Generate a form for creating new cases"""
    class Meta:
        model = NewCase
        fields = '__all__'
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'type': 'time'}),
        }


class CriminalRecordForm(forms.ModelForm):
    """Generate a form for creating new criminal records"""
    class Meta:
        model = CriminalRecord
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
        

class AddNewOfficerForm(forms.ModelForm):
    class Meta:
        model = AddNewOfficer
        fields = ['first_name', 'middle_name', 'surname', 'rank', 'username', 'password', 'status', 'badge_number']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Grace we will Perform any additional password validation here if needed
        return password
        
class LoginForm(forms.Form):
    """Class for creating a login form for the police officers"""
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())