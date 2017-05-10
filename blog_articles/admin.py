from django.contrib import admin
from django.db import models
from .models import Article, Category, Tag, Aboutme, Comments
from draceditor.widgets import AdminDraceditorWidget


# Register your models here.
# 注册models到Admin中，从而在Admin中可以操作数据
class ArticleAdmin(admin.ModelAdmin):
    # 换用DraceEditor来实现Markdown编辑器
    formfield_overrides = {
        models.TextField: {'widget': AdminDraceditorWidget},
    }
    fields = ['category', 'tag', 'author', 'title', 'abstract', 'status', 'body', 'reading', 'likes']
    list_display = ['title', 'category', 'create_time', 'modified_time', 'status', ]


class CatrgoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'modified_time', ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'content', 'user', 'published_time']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CatrgoryAdmin)
admin.site.register(Aboutme)
admin.site.register(Tag)
admin.site.register(Comments, CommentAdmin)
