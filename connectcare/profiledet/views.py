from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.decorators import login_required
from .models import USERMODEL
from .forms import UserTypeForm, ExtraForm
from django.views.generic import TemplateView, ListView, CreateView



@login_required()
def showform(request):
    p = USERMODEL.objects.filter(name = request.user.username)
    if not p:
        form = UserTypeForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = request.user.username
            request.user.usertype = obj.type
            obj.save()
        context = {'form':form}
        return render(request,'profiledet/Profile.html',context)
    else:
        p = USERMODEL.objects.get(name = request.user.username)
        if p.type == 'Doctor' and p.qual is None :
            form = ExtraForm(request.POST or None)
            if form.is_valid():
                obj = form.save(commit = False)
                p.qual = obj.qu
                p.field = obj.fi
                p.save()
            context = {'form':form}
            return render(request,'profiledet/Profile.html',context)
        else :
            context = {'type':p}
            if p.type == 'Doctor':
                return render(request,'profiledet/Doctor.html',context)
            else :
                return render(request,'profiledet/Final.html',context)
