# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# User 用户模型
# 采用的集成方式扩展用户信息
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avator/%Y/%m',default='avator/default.png',max_length=200)
    qq = models.CharField(max_length=20, blank= True, null= True ,verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank= True, null= True, unique=True,verbose_name='手机号码')

    class Meta:
        verbose_name_plural = verbose_name ='用户'
        ordering = ['-id']

    def __str__(self):
        return self.username

#tag 标签
class Tag(models.Model):
    name = models.CharField(max_length=30,verbose_name='标签名称')

    class Meta:
        verbose_name_plural = verbose_name ='标签'

    def __str__(self):
        return self.name

#catagory 分类
class Catagory(models.Model):
    name = models.CharField(max_length=30,verbose_name="分类名称")
    index = models.IntegerField(default= 999,verbose_name="分类排序")

    class Meta:
        verbose_name_plural = verbose_name = "分类"

    def __str__(self):
        return self.name

#