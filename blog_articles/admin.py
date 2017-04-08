from django.contrib import admin
from django.db import models
from .models import Aritcle, Category, Tag, Aboutme
from pagedown.widgets import AdminPagedownWidget


# Register your models here.
# 注册models到Admin中，从而在Admin中可以操作数据
class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    fields = ['category', 'Tag', 'title', 'abstract', 'status', 'body', 'reading', 'likes']
    list_display = ['title', 'category', 'create_time', 'modified_time', 'status', 'top']


admin.site.register(Aritcle, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Aboutme)
admin.site.register(Tag)
