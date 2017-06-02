from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.

class allUser(AbstractUser):
    phone = models.CharField(max_length=20, unique=True, verbose_name='手机号码')
    avatar = models.ImageField(upload_to='avatar', default='/default/ren.png',
                               verbose_name='头像')
    email = models.EmailField(max_length=200, unique=True, verbose_name='email address')

    class Meta(AbstractUser.Meta):
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'


class Private(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender')
    content = models.TextField()
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='receiver')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = '对话'
