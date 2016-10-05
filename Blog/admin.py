from django.contrib import admin
from .models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            #默认展开
            'fields':('title','desc','content',)

        }),
        ('高级设置',{
            'classes':('collapse',),
            'fields':('category','is_recommend','click_count',)
        }),

    )

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)

