from django.contrib import admin
from django.db import models
from .models import Aritcle, Category, Aboutme
from pagedown.widgets import AdminPagedownWidget


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    fields = ['category', 'title', 'abstract', 'status', 'top', 'body', 'reading', 'likes']
    list_display = ['title', 'category', 'create_time', 'modified_time', 'status', 'top']


admin.site.register(Aritcle, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Aboutme)
