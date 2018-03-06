from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
    return render(request,'profiledet/Profile.html')
