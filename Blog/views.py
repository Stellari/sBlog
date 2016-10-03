import logging
from django.shortcuts import render

logger = logging.getLogger("Blog.views")
# Create your views here.
def index(request):
    try:
        file = open("sss.txt","r")
    except Exception as e:
        logger.error(e)
    return render (request,'index.html',locals())