from django.shortcuts import render,redirect
from .models import MyUser
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.urls import reverse

# Create your views here.

def register(request):
    title='注册'
    pageTitle='用户注册'
    comfirmPassword=True
    button='注册'
    urlText='用户登录'
    urlName='userLogin'
    if request.method=='POST':
        u=request.POST.get('username','')
        p=request.POST.get('password','')
        cp=request.POST.get('cp','')
        if MyUser.objects.filter(username=u):
            tips='用户已存在'
        elif cp!=p:
            tips='两次密码输入不一致'
        else:
            d={
                'username':u, 'password':p,
                'is_superuser':1, 'is_staff':1
            }
            user=MyUser.objects.create_user(**d)
            user.save()
            tips='注册成功，可登录'
            logout(request)
            return redirect(reverse('userLogin'))
    return render(request, 'user.html', locals())

def userLogin(request):
    title='登录'
    pageTitle='用户登录'
    button='登录'
    urlText='用户注册'
    urlName='register'
    if request.method=='POST':
        u=request.POST.get('username','')
        p=request.POST.get('password','')
        if MyUser.objects.filter(username=u):
            user=authenticate(username=u,password=p)
            if user:
                if user.is_active:
                    login(request,user)
                kwargs={'id':request.user.id, 'page':1}
                return redirect(reverse('index',kwargs=kwargs))
            else:
                tips='账号密码错误'
        else:
            tips='用户不存在，请注册'
    else:
        if request.user.username:
            kwargs={'id':request.user.id, 'page':1}
            return redirect(reverse('index',kwargs=kwargs))
    return render(request, 'user.html', locals())

def about(request,id):
    user=MyUser.objects.filter(id=id).first()
    return render(request,'about.html',locals())