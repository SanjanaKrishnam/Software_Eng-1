from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiledet.models import USERMODEL
import json
from django_private_chat.models import Dialog
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


@login_required()
def pat(request):
    p = USERMODEL.objects.get(name = request.user.username)
    if p.type != 'Doctor':
        return HttpResponseRedirect('/home')
    if p.auth is None:
        p.auth = json.dumps([])
        p.save()
    jd = json.decoder.JSONDecoder()
    k = jd.decode(p.auth)
    l = []
    for obj in k:
        z = USERMODEL.objects.get(name = obj)
        l.append(z)
    return render(request,'home/patres.html',{'name':p.aname,'stuff':l})

@login_required()
def auth(request):
    p = USERMODEL.objects.get(name = request.user.username)
    if p.type != 'Patient':
        return HttpResponseRedirect('/home')
    if request.method == 'GET':
        sq = request.GET.get('docauth')
        sq = USERMODEL.objects.get(name = sq)
        if p.auth is None :
            p.auth = json.dumps([])
            p.save()
        if sq.auth is None:
            sq.auth = json.dumps([])
            sq.save()
        jd = json.decoder.JSONDecoder()
        k = jd.decode(sq.auth)
        if p.name not in k:
            k.append(p.name)
            sq.auth = json.dumps(k)
            sq.save()
            k = jd.decode(p.auth)
            k.append(sq.name)
            p.auth = json.dumps(k)
            p.save()
        user = get_object_or_404(get_user_model(), username=sq.name)
        Dialog.objects.create(owner = request.user, opponent = user)
        return render(request,'home/auth.html',{'type':sq})


@login_required()
def doc(request):
    p = USERMODEL.objects.get(name = request.user.username)
    if p.type != 'Patient':
        return HttpResponseRedirect('/home')

    if request.method == 'GET':
        sq = request.GET.get('docpr')
        if sq == None:
            return HttpResponseRedirect('/home')
        j = USERMODEL.objects.filter(name = sq)
        if not j:
            return HttpResponseRedirect('/home')
        l = USERMODEL.objects.get(name = sq)
        sq = l
        if p.auth is None or sq.auth is None:
            return render(request,'home/docprof.html',{'type':sq})
        jd = json.decoder.JSONDecoder()
        k = jd.decode(p.auth)
        if sq.name in k:
            return render(request,'home/auth.html',{'type':sq})
        return render(request,'home/docprof.html',{'type':sq})


@login_required()
def doct(request):
    p = USERMODEL.objects.get(name = request.user.username)
    if p.type != 'Patient':
        return HttpResponseRedirect('/home')
    if p.auth is None:
        p.auth = json.dumps([])
        p.save()
    jd = json.decoder.JSONDecoder()
    k = jd.decode(p.auth)
    l = []
    for obj in k:
        z = USERMODEL.objects.get(name = obj)
        l.append(z)
    return render(request,'home/docres.html',{'name':p.aname,'stuff':l})

@login_required()
def main(request):
    p = USERMODEL.objects.filter(name = request.user.username)
    if not p:
        return HttpResponseRedirect("/profile")
    k = USERMODEL.objects.get(name = request.user.username)
    if k.type == 'Public':
        return render(request,'home/Gen.html',{'name':k.aname})
    if k.type =='Patient':
        if request.method == 'GET':
            sq = request.GET.get('search_box')
            if sq !=None and sq.strip() :
                z = USERMODEL.objects.filter(name = sq,type = "Doctor")
                f = USERMODEL.objects.filter(aname = sq,type = "Doctor")
                g = USERMODEL.objects.filter(phno = sq, type = "Doctor")
                n = USERMODEL.objects.filter(qual = sq, type = "Doctor")
                p = USERMODEL.objects.filter(aname = sq, type = "Doctor")
                j = USERMODEL.objects.filter(field = sq, type = "Doctor")
                p = z|f|g|n|p|j
                return render(request,'home/rend.html',{'query':p,'name':sq})
        return render(request,'home/PAt.html',{'name':k.aname})
    if k.type == 'Doctor':
        return render(request,'home/Doc.html',{'name':k.aname})
