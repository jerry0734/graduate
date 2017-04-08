from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Aritcle, Category, Aboutme, Tag
import markdown_deux
import markdown2


class IndexView(ListView):
    """博客主页文章列表"""
    template_name = "blog_articles/index.html"

    context_object_name = "article_list"

    # 返回文章
    def get_queryset(self):
        article_list = Aritcle.objects.filter(status='p')
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)


def aboutme(request):
    """显示关于博客的页面"""

    # 只取第一条数据
    about = Aboutme.objects.get(id=1)
    context = {'about': about}
    return render(request, 'blog_articles/aboutme.html', context)
