from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from profiledet.models import USERMODEL
from .models import Document
from .forms import DocumentForm
from django.http import HttpResponseRedirect
@login_required()
def home(request):
    p = USERMODEL.objects.filter(name = request.user.username)
    if not p:
        return HttpResponseRedirect("/home")
    k = USERMODEL.objects.get(name = request.user.username)
    if k.type == 'Patient':
        documents = Document.objects.filter(user = request.user.username, location = 'Med_HIST')
        return render(request, 'uploads/home.html', { 'documents': documents })
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
            a.user = request.user.username
            a.description = filename
            a.location = 'Med_HIST'
            a.save()
            return render(request, 'uploads/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,'name':filename
            })
        return render(request, 'uploads/simple_upload.html')
    else :
        return HttpResponseRedirect("/home")
