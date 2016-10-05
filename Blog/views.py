import logging
from django.shortcuts import render
from django.conf import settings
from .models import *

logger = logging.getLogger("Blog.views")
# Create your views here.
def global_setting(request):
    return {'SITE_NAME':settings.SITE_NAME,
            'SITE_DESC': "Stellari练手的博客，欢迎修改",}

def index(request):
    try:
        article_list = Article.objects.all()
    except Exception as e:
        logger.error(e)
    return render (request,'index.html',{'ariticle_list': article_list},)