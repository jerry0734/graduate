from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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
        # 增加额外的数据，这里返回一个文章分类，以字典的形式
        # 显示前五项最新修改的分类
        kwargs['category_list'] = Category.objects.order_by('modified_time')[0:5]
        return super(IndexView, self).get_context_data(**kwargs)


class ArticleDetailView(DetailView):
    model = Aritcle

    template_name = "blog_articles/article.html"

    context_object_name = "article"

    pk_url_kwarg = 'article_id'

    # get_object() 返回该视图要显示的对象
    def get_object(self):
        context = super(ArticleDetailView, self).get_object()
        return context


def aboutme(request):
    """显示关于博客的页面"""

    # 只取第一条数据
    about = Aboutme.objects.all()[0]
    context = {'about': about}
    return render(request, 'blog_articles/aboutme.html', context)
