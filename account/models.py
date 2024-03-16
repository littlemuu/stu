from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    name=models.CharField('姓名',max_length=50,default='匿名用户')
    classnumber=models.CharField('班级',max_length=50,default='未知')
    subject=models.CharField('科目',max_length=50,default='未知')
    email=models.CharField('邮箱',max_length=100,default='未知')