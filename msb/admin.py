from django.contrib import admin
from msb.models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ['content', 'author_name', 'published_time', ]


admin.site.register(Message)
