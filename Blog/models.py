# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 自定义过滤器
class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y/%M文章存档')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list

# User 用户模型
# 采用的集成方式扩展用户信息
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avator/%Y/%m/%d',default='avator/default.png',max_length=200,blank=True,null=True,verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank= True, null= True ,verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank= True, null= True, unique=True,verbose_name='手机号码')

    class Meta:
        verbose_name_plural = verbose_name ='用户'
        ordering = ['-id']

    def __str__(self):
        return self.username

#tag 标签
class Tag(models.Model):
    name = models.CharField(null= True,max_length=30,verbose_name='标签名称')

    class Meta:
        verbose_name_plural = verbose_name ='标签'

    def __str__(self):
        return self.name

#catagory 分类
class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name="分类名称")
    index = models.IntegerField(default= 999,verbose_name="分类排序")

    class Meta:
        verbose_name_plural = verbose_name = "分类"

    def __str__(self):
        return self.name

# Article 文章模型
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="文章标题")
    desc = models.CharField(max_length=50, verbose_name="文章描述",null=True)
    content = models.TextField(verbose_name="文章内容",null=True)
    click_count = models.IntegerField(default=0, verbose_name="点击次数",null=True)
    is_recommend = models.BooleanField(default=False,verbose_name="被推荐")
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name="发布时间",null=True)
    user = models.ForeignKey(User,verbose_name="用户",null=True)
    category = models.ForeignKey(Category, blank=True, null=True,verbose_name="文章分类")
    tag = models.ManyToManyField(Tag,verbose_name="标签",null=True)

    objects = ArticleManager()

    class Meta:
        verbose_name_plural = verbose_name="文章"
        ordering =['-date_publish']

    def __str__(self):
        return self.title

# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name="评论内容")
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name="发布日期")
    user = models.ForeignKey(User, null= True, blank=True,verbose_name="用户名")
    article = models.ForeignKey(Article,blank=True,null=True,verbose_name="文章")
    pid = models.ForeignKey('self',blank=True,null=True,verbose_name="父级评论")

    class Meta:
        verbose_name_plural =verbose_name ='评论'
        ordering = ['-date_publish']

    def __str__(self):
        return str(self.id)

# Links 友情链接
class Links(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    desc = models.CharField(max_length=200,verbose_name="描述")
    callback_url = models.URLField(verbose_name="URL地址")
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    index = models.IntegerField(default=999, verbose_name="排列顺序")

    class Meta:
        verbose_name_plural =verbose_name ='友情链接'

    def __str__(self):
        return self.title

# Ad 广告
class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='广告')
    desc = models.CharField(max_length=200, verbose_name="描述")
    img_url = models.ImageField(upload_to='ad/%Y/%m',verbose_name='图片路径')
    callback_url = models.URLField(null=True,blank=True,verbose_name="链接URL")
    index = models.IntegerField(default=999, verbose_name='排列顺序')

    class Meta:
        verbose_name_plural = verbose_name ='广告'
        ordering = ['index','id']

    def __str__(self):
        return self.title

