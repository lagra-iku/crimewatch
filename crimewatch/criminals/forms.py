from django import forms
from .models import CriminalRecord

class CriminalForm(forms.ModelForm):
    class Meta:
        model = CriminalRecord
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_of_arrest': forms.DateInput(attrs={'type': 'date'}),
            'time_of_arrest': forms.TimeInput(attrs={'type': 'time'}),
        }