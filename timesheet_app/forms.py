from django import forms
from .models import StaffDetails, CustomUser

class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffDetails
        fields = '__all__'

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'access_level', 'location', 'region']

from .models import TimesheetEntry
from django import forms

class TimesheetEntryForm(forms.ModelForm):
    class Meta:
        model = TimesheetEntry
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time_in': forms.TimeInput(attrs={'type': 'time'}),
            'time_out': forms.TimeInput(attrs={'type': 'time'}),
        }
