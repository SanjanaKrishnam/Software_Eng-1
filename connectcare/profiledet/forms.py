from django import forms
from .models import USERMODEL

class UserTypeForm(forms.ModelForm):
    class Meta:
        model = USERMODEL
        fields = ['type']
