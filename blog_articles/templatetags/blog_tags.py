from ..models import Article
from django.template import Library

# 注册标签，不注册会出事（手动滑稽）
register = Library()


# 文章归档主页标签
@register.simple_tag
def archives():
    return Article.objects.dates('create_time', 'year', order='DESC')
