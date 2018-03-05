from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from .models import Document
from .forms import DocumentForm

@login_required()
def home(request):
    documents = Document.objects.filter(user = request.user.username)
    return render(request, 'uploads/home.html', { 'documents': documents })

@login_required()
def upl(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        a = Document()
        a.document.name = filename
        a.user = request.user.username
        a.description = filename
        a.save()
        return render(request, 'uploads/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,'name':filename
        })
    return render(request, 'uploads/simple_upload.html')
