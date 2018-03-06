from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'mysite/home.html')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/profile')
            else:
                messages.info(request,'Username or e-mail id has already been registered')
                form = UserRegistrationForm()
    else:
        form = UserRegistrationForm()
    return render(request, 'mysite/register.html', {'form' : form})
