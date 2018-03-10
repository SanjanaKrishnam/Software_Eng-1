from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from profiledet.models import USERMODEL
from .models import Testres
from django.http import HttpResponseRedirect
import json


patientname = None

@login_required
def docfin(request):
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
        global patientname
        patientname = sq
        j = USERMODEL.objects.get(name = sq)
        return render(request,'testres/DoctorUploadMain.html',{'name':j.aname})
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        a = Testres()
        a.document.name = filename
        a.user = p.name
        a.description = filename
        a.location = 'TestRes'
        a.save()
        return render(request, 'testres/DoctorUploadMain.html', {
        'uploaded_file_url': uploaded_file_url,'name':filename
        })


@login_required
def testup(request):
    p = USERMODEL.objects.filter(name = request.user.username)
    if not p:
        return HttpResponseRedirect("/home")
    p = USERMODEL.objects.get(name= request.user.username)
    if p.type!='Doctor':
        return HttpResponseRedirect("/home")
    if request.method =='GET':
        sq = request.GET.get('Pat_test_up')
        if sq == None:
            return HttpResponseRedirect('/home')
        j = USERMODEL.objects.filter(name = sq)
        if not j:
            return HttpResponseRedirect('/home')
        j = USERMODEL.objects.get(name = sq)
        k = Testres.objects.filter(user = p.name)
        return render(request,'testres/DoctorUploadHome.html',{'name':j.aname,'user':j.name,'documents':k})

@login_required
def main(request):
    p = USERMODEL.objects.filter(name = request.user.username)
    if not p:
        return HttpResponseRedirect("/home")
    p = USERMODEL.objects.get(name= request.user.username)
    if p.type=='Public':
        return HttpResponseRedirect("/home")
    if p.type == 'Patient':
        return render(request,"testres/pat.html")
    else:
        jd = json.decoder.JSONDecoder()
        if p.auth is None:
            p.auth = json.dumps([])
            p.save()
        k = jd.decode(p.auth)
        l = []
        for obj in k:
            z = USERMODEL.objects.get(name = obj)
            l.append(z)
        return render(request,'testres/doc.html',{'name':p.aname,'stuff':l})
