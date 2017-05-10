from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.db.models import Count
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from myuser.models import allUser
from .models import Article, Category, Aboutme, Tag, Comments
from .forms import CommentForm, ArticleForm
from haystack.forms import SearchForm
from django.core.urlresolvers import reverse


class IndexView(ListView):
    """博客主页文章列表"""
    template_name = "blog_articles/index.html"

    context_object_name = "article_list"

    # 返回文章
    def get_queryset(self):
        article_list = Article.objects.filter(status='p').order_by('-create_time')
        return article_list

    def get_context_data(self, **kwargs):
        # 增加额外的数据，这里返回一个文章分类，以字典的形式
        # 显示前五项最新修改的分类
        kwargs['category_list'] = Category.objects.order_by('-modified_time')[0:5]
        # 标签列表
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)


class ArticleDetailView(DetailView):
    """文章详情页视图"""
    model = Article

    template_name = "blog_articles/article.html"

    context_object_name = "article"

    pk_url_kwarg = 'article_id'

    # get_object() 返回该视图要显示的对象
    def get_object(self):
        context = super(ArticleDetailView, self).get_object()
        return context

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['form'] = CommentForm()
        kwargs['comment_list'] = self.object.comments_set.all()
        return super(ArticleDetailView, self).get_context_data(**kwargs)


class CategoryView(ListView):
    """单个分类下的文章列表视图--类形式"""

    template_name = "blog_articles/category.html"
    # 指定需要渲染的模板

    context_object_name = "article_list"

    # 指定模板中需要使用的上下文对象的名字

    def get_queryset(self):
        # get_queryset 的作用已在第一篇中有介绍，不再赘述
        article_list = Article.objects.filter(category=self.kwargs['category_id'], status='p')
        # 使用了分类的id作为关键字参数（category_id）传递给了CategoryView，传递的参数在kwargs属性中获取。
        return article_list

    # 给视图增加额外的数据
    def get_context_data(self, **kwargs):
        # 增加一个category_list,用于在页面显示所有分类，按照名字排序
        kwargs['category_list'] = Category.objects.all().order_by('name')
        # 获取正确的分类id，以便在标题栏正确显示分类名称
        kwargs['category'] = Category.objects.get(id=self.kwargs['category_id'])
        # 统计分类下的文章数量
        kwargs['count'] = Category.objects.annotate(num=Count('article'))
        return super(CategoryView, self).get_context_data(**kwargs)


class Tagview(ListView):
    template_name = 'blog_articles/tag.html'

    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(tag=self.kwargs['tag_id'], status='p')
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['tag'] = Tag.objects.get(id=self.kwargs['tag_id'])
        return super(Tagview, self).get_context_data(**kwargs)


# 单个分类下的文章列表视图-次选-函数形式
# def categoryview(request, category_id):
#     category = Category.objects.get(id=category_id)
#     article_list = category.article_set.order_by('-modified_time')
#     context = {'category': category, 'article_list': article_list}
#     return render(request, 'blog_articles/category.html', context)

def aboutme(request):
    """显示关于博客的页面"""

    # 只取第一条数据
    about = Aboutme.objects.all()[0]
    context = {'about': about}
    return render(request, 'blog_articles/aboutme.html', context)


def showcategories(request):
    """分类主页面"""
    # 分类下没有文章不显示
    category_list = Category.objects.all().annotate(num_articles=Count('article')).filter(num_articles__gt=0)
    # count = Category.objects.annotate(num=Count('article'))
    tag_list = Tag.objects.all()
    context = {'category_list': category_list, 'tag_list': tag_list, }
    return render(request, 'blog_articles/categories.html', context)


def archive(request, year):
    """日期归档视图函数"""
    article_list = Article.objects.filter(create_time__year=year)
    category_list = Category.objects.all().order_by('-modified_time')[0:5]
    tag_list = Tag.objects.all().order_by('name')
    context = {'article_list': article_list, 'category_list': category_list,
               'tag_list': tag_list}
    return render(request, 'blog_articles/index.html', context)


def write_comments(request, article_id):
    """评论"""
    if request.method != 'POST':
        form = CommentForm()

    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            article = Article.objects.get(id=article_id)
            user = request.user
            comment = form.save(commit=False)
            comment.article = article
            comment.user = user
            form.save()
            # return redirect(to='article', id=article_id)
            return redirect('blog:detail', article_id=article_id)

    return redirect('blog:detail', article_id=article_id)


def edit_comment(request):
    """修改评论"""
    # todo:修改评论
    pass


def delete_comment(request):
    """删除评论"""
    # todo:删除评论
    pass


def add_category(request):
    """添加分类"""
    # todo：添加分类
    pass


def add_tag(request):
    """添加标签"""
    # todo：添加标签
    pass


def edit_category(request):
    """修改分类"""
    # todo:修改分类
    pass

def search_article(request):
    """文章搜索"""
    keyword = request.GET['q']
    form = SearchForm(request.GET)
    articles = form.search()
    messages = '关键字 \'{}\' 搜索结果'.format(keyword)
    context = {
        'articles': articles,
        'messages': messages,
    }
    return render(request, 'blog_articles/article_search.html', context)


@login_required
def management_index(request):
    """后台管理索引主页，用于引导管理界面"""
    if allUser.is_superuser:
        return render(request, 'blog_articles/management/manage_index.html', {})
    else:
        raise Http404


@login_required
def new_article(request):
    """添加新文章"""
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            new_article = form.save()
            return HttpResponseRedirect(reverse('blog:index'))

    context = {'form': form}
    return render(request, 'blog_articles/new_article.html', context)


@login_required
def edit_article(request, article_id):
    """编辑文章"""
    article = Article.objects.get(id=article_id)
    if request.method != 'POST':
        form = ArticleForm(instance=article)
    else:
        form = ArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:detail', args=[article_id]))
    context = {'form': form, 'article': article}

    return render(request, 'blog_articles/edit_article.html', context)
