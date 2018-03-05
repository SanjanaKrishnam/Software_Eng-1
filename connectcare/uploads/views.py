from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Document
from .forms import DocumentForm

def home(request):
    documents = Document.objects.all()
    return render(request, 'uploads/home.html', { 'documents': documents })


def upl(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploads/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'uploads/simple_upload.html')
