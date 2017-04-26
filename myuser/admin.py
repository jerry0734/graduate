from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import allUser

# Register your models here.
admin.site.register(allUser, UserAdmin)
