from django.db import models
from account.models import MyUser

# Create your models here.

class Students_info(models.Model):
    number=models.CharField('学号',max_length=10,default='未知')
    stu_name=models.CharField('学生姓名',max_length=50,default='未知')
    teacher=models.ForeignKey(MyUser,on_delete=models.CASCADE,verbose_name='老师姓名')
    score=models.FloatField('分数',default='未录入')