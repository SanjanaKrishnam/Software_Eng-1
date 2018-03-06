from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.decorators import login_required
from .models import USERMODEL
from .forms import UserTypeForm
from django.views.generic import TemplateView, ListView, CreateView


class CreateMyModelView(CreateView):
    model = USERMODEL
    form_class = UserTypeForm
    template_name = 'profiledet/Profile.html'
