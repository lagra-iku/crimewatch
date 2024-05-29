from django import forms
from .models import CriminalRecord

class CriminalForm(forms.ModelForm):
    date_of_arrest = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CriminalRecord
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_of_arrest': forms.DateInput(attrs={'type': 'date'}),
            'time_of_arrest': forms.TimeInput(attrs={'type': 'time'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(CriminalForm, self).__init__(*args, **kwargs)
        # if not self.instance.pk:
        #     self.fields['case_number'].widget.attrs['readonly'] = True
        #     self.fields['case_number'].widget.attrs['class'] = 'form-control-plaintext'

        # if 'crime_type' in self.data:
        #     try:
        #         crime_type_id = int(self.data.get('crime_type'))
        #         self.fields['crime_subcategory'].queryset = crime_subcategory.objects.filter(crime_type_id=crime_type_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass
        # elif self.instance.pk and self.instance.crime_type:
        #     self.fields['crime_subcategory'].queryset = self.instance.crime_type.subcategories.order_by('name')   
