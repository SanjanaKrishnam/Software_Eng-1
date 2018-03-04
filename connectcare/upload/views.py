from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms

from django.contrib import messages
# Create your views here.
def upload(request):
    return render(request, 'mysite/upload.html')
