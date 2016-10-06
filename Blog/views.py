import logging
from django.shortcuts import render
from django.conf import settings
from .models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

logger = logging.getLogger("Blog.views")
# Create your views here.
def global_setting(request):
    return {'SITE_NAME':settings.SITE_NAME,
            'SITE_DESC': "Stellari练手的博客，欢迎修改",}

def index(request):
    try:
        #文章
        article_list = Article.objects.all()
        # 广告数据
        ad_list = Ad.objects.all()
        #分类目录
        category_list = Category.objects.all()
        #标签分类
        tag_list = Tag.objects.all()


    except Exception as e:
        logger.error(e)
    return render (request,'index1.html',locals(),)