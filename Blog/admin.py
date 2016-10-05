from django.contrib import admin
from .models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title','desc','content',)

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)

