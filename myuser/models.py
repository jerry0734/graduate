from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class gusetUser(AbstractUser):
    avatar = models.CharField(max_length=255, default='/static/amaze-assets/i/ren.png',
                              verbose_name='头像')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='手机号码')

    class Meta(AbstractUser.Meta):
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'
