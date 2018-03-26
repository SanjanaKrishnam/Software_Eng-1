from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from profiledet.models import USERMODEL
from django.http import HttpResponseRedirect
import json
from django.http import HttpResponse


@login_required()
def main(request):
    p = USERMODEL.objects.filter(name = request.user.username)
    if not p:
        return HttpResponseRedirect("/home")
    k = USERMODEL.objects.get(name = request.user.username)
    if k.type == 'Public':
        return HttpResponseRedirect("/home")
    if k.type == 'Doctor':
        return render(request,'presc/Doctorfirst.html')
    else :
        return render(request,'presc/Patient.html')
