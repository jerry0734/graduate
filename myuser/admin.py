from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import allUser, Private

# Register your models here.
class MyUserAdmin(UserAdmin):
    fieldsets = (
        ('个人信息', {
            'fields': ('username', 'password', 'email', 'phone', 'avatar')
        }),
        ('姓名', {
            'fields': ('first_name', 'last_name')
        }),
        ('权限', {
            'fields': ('is_superuser', 'is_staff', 'is_active')
        }),
        ('', {
            'fields': ('date_joined', 'last_login',)
        }),
        ('', {
            'fields': ('groups', 'user_permissions',)
        }),
    )


# admin.site.register(allUser, MyUserAdmin)
admin.site.register(allUser, MyUserAdmin)
admin.site.register(Private)
