from django.db import models


# Create your models here.

# 创建博客主题模型
class Aritcle(models.Model):
    """博客主体，内包含文章，编者，发布状态与时间等等"""

    # Field.choices
    # 选择器，可以选择
    PUBLISH_STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发布'),
    )

    # 文章标题，max_length为标题最大长度
    # '标题'是一个位置参数，admin后台管理提示符
    title = models.CharField('文章标题', max_length=70)

    # 文章主体
    # '正文'的作用同上，都只是用于admin管理界面
    body = models.TextField('正文')

    # 创建时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    # 修改时间
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    # 文章发布状态
    status = models.CharField('发布状态', max_length=1, choices=PUBLISH_STATUS_CHOICES)

    # todo:文章摘要

    # todo:文章被浏览次数
    # TODO：文章点赞数
    # TODO：文章被置顶状态


class Category(models.Model):
    """文章分类"""
    pass