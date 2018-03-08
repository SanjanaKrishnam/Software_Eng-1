from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiledet.models import USERMODEL

@login_required()
def main(request):
    p = USERMODEL.objects.filter(name = request.user.username)
    if not p:
        return render(request,'home/Gen.html')
    k = USERMODEL.objects.get(name = request.user.username)
    if k.type == 'Public':
        return render(request,'home/Gen.html')
    if k.type =='Patient':
        if request.method == 'GET':
            sq = request.GET.get('search_box')
            if sq !=None and sq.strip() :
                return render(request,'home/rend.html',{'query':sq})
        return render(request,'home/PAt.html')
    if k.type == 'Doctor':
        return render(request,'home/Doc.html')
