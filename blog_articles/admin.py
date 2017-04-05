from django.contrib import admin
from django.db import models
from .models import Aritcle, Category
from pagedown.widgets import AdminPagedownWidget


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    # models.TextField: {'widget': AdminPagedownWidget },
    # }
    fields = ['category', 'title', 'abstract', 'status', 'top', 'body', 'reading', 'likes']

    class Media:
        js = (
            'js/jquery-3.2.0.min.js',
            'editormd/editormd.min.js',
            'editormd/editormd.amd.min.js'
        )
        css = {
            'all': ('editormd/css/editormd.css',),
        }


admin.site.register(Aritcle, ArticleAdmin)
admin.site.register(Category)
