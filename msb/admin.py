from django.contrib import admin
from msb.models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'email','published_time', ]


admin.site.register(Message, MessageAdmin)
