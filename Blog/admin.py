from django.contrib import admin
from .models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','desc','click_count',)
    fieldsets = (
        (None,{
            #默认展开
            'fields':('title','desc','content',)

        }),
        ('高级设置',{
            'classes':('collapse',),
            'fields':('category','is_recommend','click_count','tag',)
        }),

    )

    class Media:
        js =(
            'js/kindeditor/kindeditor-min.js',
            'js/kindeditor/lang/zh_CN.js',
            'js/kindeditor/config.js',
        )

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)

