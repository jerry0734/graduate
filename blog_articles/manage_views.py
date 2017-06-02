from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.db.models import Count
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from myuser.models import allUser
from .models import Article, Category, Aboutme, Tag, Comments, Friends
from .forms import CommentForm, ArticleForm, CategoryForm, TagForm, AboutForm, TitlePhotoForm
from haystack.forms import SearchForm
from django.core.urlresolvers import reverse
from .forms import LinkForm


@login_required
def management_index(request):
    """后台管理索引主页，用于引导管理界面"""
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('blog:myarticles'))
    else:
        raise Http404


@login_required
def myarticles(request):
    """文章列表"""
    articles = Article.objects.filter(author=request.user)
    form = TitlePhotoForm()
    context = {'article_list': articles, 'form': form}
    return render(request, 'blog_articles/newmanage/myarticles.html', context)


@login_required
def new_article(request):
    """添加新文章"""
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            new_article = form.save()
            return HttpResponseRedirect(reverse('blog:myarticles'))

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


def delete_article(request, article_id):
    """删除文章"""
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('blog:myarticles')


def article_comment(request, article_id):
    """文章下的评论列表"""
    comments = Comments.objects.filter(article_id=article_id)
    context = {'comment_list': comments}
    return render(request, 'blog_articles/management/article_comment.html', context)


@login_required
def edit_comment(request, comment_id):
    """管理界面修改评论"""
    comment = Comments.objects.get(id=comment_id)
    article_id = comment.article_id
    if request.method != "POST":
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:article_comment', article_id=article_id)
    context = {'comment_form': form, 'comment': comment, 'article': article_id}
    return render(request, 'blog_articles/management/edit_comment.html', context)


def delete_comment(request, comment_id):
    """管理界面删除评论"""
    comment = Comments.objects.get(id=comment_id)
    article_id = comment.article_id
    comment.delete()
    a = request.path
    print(a)
    return redirect('blog:article_comment', article_id=article_id)


@login_required
def manage_category(request):
    """分类列表"""
    category_list = Category.objects.all().order_by('modified_time')
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:category_list'))
    context = {'category_list': category_list,
               'form': form, }
    return render(request, 'blog_articles/newmanage/category_manage.html', context)


@login_required
def edit_category(request, category_id):
    """修改分类"""
    category = Category.objects.get(id=category_id)
    if request.method != "POST":
        form = CategoryForm(instance=category)
    else:
        form = CategoryForm(instance=category, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:category_list'))

    context = {'form': form, 'category': category}
    return render(request, 'blog_articles/management/edit_category.html', context)


@login_required
def delete_category(request, category_id):
    """删除分类"""
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('blog:category_list')


@login_required
def manage_tags(request):
    """标签列表"""
    tag_list = Tag.objects.all().order_by('name')
    if request.method != 'POST':
        form = TagForm()
    else:
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:tag_list'))

    context = {'tag_list': tag_list, 'tagform': form}
    return render(request, 'blog_articles/newmanage/tag_manage.html', context)


@login_required
def edit_tag(request, tag_id):
    """修改标签"""
    tag = Tag.objects.get(id=tag_id)
    if request.method != "POST":
        form = TagForm(instance=tag)
    else:
        form = TagForm(instance=tag, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:tag_list'))

    context = {'form': form, 'tag': tag}
    return render(request, 'blog_articles/management/edit_tag.html', context)


@login_required
def delete_tag(request, tag_id):
    """删除标签"""
    tag = Tag.objects.get(id=tag_id)
    tag.delete()
    return redirect('blog:tag_list')


@login_required
def edit_aboutme(request, id):
    """修改关于博客信息"""
    about = Aboutme.objects.get(id=id)
    if request.method != 'POST':
        form = AboutForm(instance=about)
    else:
        form = AboutForm(data=request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect('blog:edit_aboutme', id=id)
    context = {'about': about, 'form': form}
    return render(request, 'blog_articles/newmanage/edit_aboutme.html', context)


@login_required
def friendlink(request):
    """友链列表"""
    link_list = Friends.objects.all()
    if request.method != "POST":
        form = LinkForm()
    else:
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:link_list'))
    context = {'link_list': link_list,
               'form': form, }
    return render(request, 'blog_articles/newmanage/link_list.html', context)


@login_required
def delete_friends(request, friends_id):
    # 删除友链
    link = Friends.objects.get(id=friends_id)
    link.delete()
    return redirect('blog:link_list')


@login_required
def change_titlephoto(request, article_id):
    if request.method != 'POST':
        form = TitlePhotoForm()
    else:
        article = Article.objects.get(id=article_id)
        form = TitlePhotoForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:myarticles'))
    return None


def page_not_found(request):
    return render(request, 'blog_articles/404.html')
