from django import forms
from .models import Criminal

class CriminalForm(forms.ModelForm):
    class Meta:
        model = Criminal
        fields = '__all__'