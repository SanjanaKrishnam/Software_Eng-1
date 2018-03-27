from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from profiledet.models import USERMODEL
from django.http import HttpResponseRedirect
import json
from django.http import HttpResponse
from .models import Presc
from .forms import PrescriptionForm

@login_required()
def upl(request):
    p = USERMODEL.objects.filter(name = request.user.username)
    if not p:
        return HttpResponseRedirect("/home")
    p = USERMODEL.objects.get(name= request.user.username)
    if p.type!='Doctor':
        return HttpResponseRedirect("/home")
    if request.method =='GET':
        sq = request.GET.get('uploadtest')
        if sq == None:
            return HttpResponseRedirect('/home')
        j = USERMODEL.objects.filter(name = sq)
        if not j:
            return HttpResponseRedirect('/home')
        j = USERMODEL.objects.get(name = sq)
        form = PrescriptionForm(request.POST or None)
        context = {'form':form,'names':j.aname,'set':j.name}
        return render(request,'presc/Doctor3rd.html',context)
    if request.method == 'POST':
        sq = request.POST.get('uploadtest')
        form = PrescriptionForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.doctor = request.user.username
            obj.patient = sq
            obj.save()
            k = '/presc/Patup?Pat_up='
            k = k+str(sq)
            return HttpResponseRedirect(k)


@login_required()
def patup(request):
    p = USERMODEL.objects.filter(name = request.user.username)
    if not p:
        return HttpResponseRedirect("/home")
    p = USERMODEL.objects.get(name= request.user.username)
    if p.type!='Doctor':
        return HttpResponseRedirect("/home")
    if request.method =='GET':
        sq = request.GET.get('Pat_up')
        if sq == None:
            return HttpResponseRedirect('/home')
        j = USERMODEL.objects.filter(name = sq)
        if not j:
            return HttpResponseRedirect('/home')
        j = USERMODEL.objects.get(name = sq)
        k = Presc.objects.filter(patient = j.name)
        return render(request,'presc/Doctor2nd.html',{'name':j.aname,'user':j.name,'documents':k})

@login_required()
def main(request):
    p = USERMODEL.objects.filter(name = request.user.username)

    if not p:
        return HttpResponseRedirect("/home")
    p = USERMODEL.objects.get(name = request.user.username)
    if p.type == 'Public':
        return HttpResponseRedirect("/home")
    if p.type == 'Doctor':
        jd = json.decoder.JSONDecoder()
        if p.auth is None:
            p.auth = json.dumps([])
            p.save()
        k = jd.decode(p.auth)
        l = []
        for obj in k:
            z = USERMODEL.objects.get(name = obj)
            l.append(z)
        return render(request,'presc/Doctorfirst.html',{'name':p.aname,'stuff':l})
    else :
        k = Presc.objects.filter(patient = p.name)
        return render(request,'presc/Patient.html',{'documents':k})
