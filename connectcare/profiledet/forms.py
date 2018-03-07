from django import forms
from .models import USERMODEL
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import DateInput

class UserTypeForm(forms.ModelForm):
    #lop = DateField(widget=AdminDateWidget)
    class Meta:
        model = USERMODEL
        labels = {'aname':'Name','type':'Account Type','phno':'Mobile Number','dob':'Date of Birth','bg':'Blood Group'}
        fields = ['aname','type','phno','dob','bg']
        widgets={
        'dob': DateInput(attrs={'type':'date'})
        }
