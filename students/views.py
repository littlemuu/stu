from django.shortcuts import render,redirect
from account.models import MyUser
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from .models import Students_info
from django.urls import reverse

# Create your views here.

def students(request,id,page):
    stu=Students_info.objects.filter(teacher_id=id)
    user=MyUser.objects.filter(id=id).first()
    if not user:
        return redirect(reverse('register'))
    ats=Students_info.objects.filter(teacher_id=id)
    Paginator=Paginator(ats,10)
    try:
        pageInfo=Paginator.page(page)
    except PageNotAnInteger:
        pageInfo=Paginator.page(10)
    except EmptyPage:
        pageInfo=Paginator.page(Paginator.num_pages)
    return render(request,'students.html',locals())