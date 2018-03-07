from django import forms
from .models import USERMODEL

class UserTypeForm(forms.ModelForm):
    class Meta:
        model = USERMODEL
        labels = {'aname':'Username','type':'Account Type','phno':'Mobile Number','dob':'Date of Birth','bg':'Blood Group'}
        fields = ['aname','type','phno','dob','bg']
