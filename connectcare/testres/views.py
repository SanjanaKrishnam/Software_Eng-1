from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from profiledet.models import USERMODEL
from .models import Testres
from django.http import HttpResponseRedirect
import json


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
        return 

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
            z = USERMODEL.objects.get(aname = obj)
            l.append(z)
        return render(request,'testres/doc.html',{'name':p.aname,'stuff':l})
