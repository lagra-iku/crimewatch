from django import forms
from .models import PoliceOfficers


class PoliceOfficersForm(forms.ModelForm):
    class Meta:
        model = PoliceOfficers
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }