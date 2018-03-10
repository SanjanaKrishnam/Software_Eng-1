from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from profiledet.models import USERMODEL
from .models import Document
from .forms import DocumentForm
from django.http import HttpResponseRedirect
import json
@login_required()
def home(request):
    p = USERMODEL.objects.filter(name = request.user.username)
    if not p:
        return HttpResponseRedirect("/home")
    k = USERMODEL.objects.get(name = request.user.username)
    if k.type == 'Patient':
        documents = Document.objects.filter(user = request.user.username, location = 'Med_HIST')
        return render(request, 'uploads/home.html', { 'documents': documents })
    elif k.type =='Doctor':
        jd = json.decoder.JSONDecoder()
        if k.auth == None:
            k.auth = json.dumps([])
            k.save()
        liste = jd.decode(k.auth)
        L = Document.objects.filter(user = liste[0],location = 'Med_HIST')
        for obj in liste:
            k = Document.objects.filter(user = obj, location = 'Med_HIST')
            L = L|k
        return render(request,'uploads/docview.html',{'documents':L})
    else:
        return HttpResponseRedirect("/home")


@login_required()
def upl(request):
    p = USERMODEL.objects.filter(name = request.user.username)
    if not p:
        return HttpResponseRedirect("/home")
    k = USERMODEL.objects.get(name = request.user.username)
    if k.type == 'Patient':
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            a = Document()
            a.document.name = filename
            a.user = k.name
            a.description = filename
            a.location = 'Med_HIST'
            a.save()
            return render(request, 'uploads/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,'name':filename
            })
        return render(request, 'uploads/simple_upload.html')
    else :
        return HttpResponseRedirect("/home")
