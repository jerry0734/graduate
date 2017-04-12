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
        kwargs['category_list'] = Category.objects.order_by('-modified_time')[0:5]
        return super(IndexView, self).get_context_data(**kwargs)


class ArticleDetailView(DetailView):
    """文章详情页视图"""
    model = Aritcle

    template_name = "blog_articles/article.html"

    context_object_name = "article"

    pk_url_kwarg = 'article_id'

    # get_object() 返回该视图要显示的对象
    def get_object(self):
        context = super(ArticleDetailView, self).get_object()
        return context

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        # 增加一个category_list,用于在页面显示所有分类，按照名字排序
        return super(ArticleDetailView, self).get_context_data(**kwargs)


# class CategoryView(ListView):
#     template_name = "blog_articles/category.html"
#     # 指定需要渲染的模板
#
#     context_object_name = "article_list"
#
#     # 指定模板中需要使用的上下文对象的名字
#
#     def get_queryset(self):
#         # get_queryset 的作用已在第一篇中有介绍，不再赘述
#         article_list = Aritcle.objects.filter(category=self.kwargs['category_id'], status='p')
#         # 注意在url里我们捕获了分类的id作为关键字参数（cate_id）传递给了CategoryView，传递的参数在kwargs属性中获取。
#         return article_list
#
#     # 给视图增加额外的数据
#     def get_context_data(self, **kwargs):
#         kwargs['category_list'] = Category.objects.all().order_by('name')
#         # 增加一个category_list,用于在页面显示所有分类，按照名字排序
#         return super(CategoryView, self).get_context_data(**kwargs)

def aboutme(request):
    """显示关于博客的页面"""

    # 只取第一条数据
    about = Aboutme.objects.all()[0]
    context = {'about': about}
    return render(request, 'blog_articles/aboutme.html', context)


def showcategories(request):
    """分类主页面"""
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return render(request, 'blog_articles/categories.html', context)


def categoryview(request, category_id):
    category = Category.objects.get(id=category_id)
    article_list = category.aritcle_set.order_by('-modified_time')
    context = {'category': category, 'article_list': article_list}
    return render(request, 'blog_articles/category.html', context)
