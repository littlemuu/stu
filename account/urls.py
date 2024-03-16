from django.urls import path
from .views import *
urlpatterns = [
    #注册
    path('register.html', register ,name='register'),
    #登录
    path('login.html', userLogin ,name='userLogin'),

    #用户个人页面
    path('about/<int:id>.html',about,name='about'),
]
