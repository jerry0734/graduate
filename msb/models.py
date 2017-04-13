from django.db import models


# Create your models here.

class Message(models.Model):
    """留言板model"""

    # 电子邮件
    email = models.EmailField('电子邮件地址')

    # 留言者名称
    author_name = models.CharField('姓名', max_length=20)

    # 内容
    content = models.TextField('正文')

    # 时间
    published_time = models.DateTimeField('发表时间', auto_now_add=True)

    def __str__(self):
        # 控制显示长度
        if len(self.content) <= 50:
            return self.content
        else:
            return self.content[:50] + "..."

    class Meta:
        ordering = ['-published_time']
        verbose_name_plural = '留言'
