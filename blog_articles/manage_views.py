from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.db.models import Count
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from myuser.models import allUser
from .models import Article, Category, Aboutme, Tag, Comments, Friends
from .forms import CommentForm, ArticleForm, CategoryForm, TagForm, AboutForm
from haystack.forms import SearchForm
from django.core.urlresolvers import reverse
from .forms import LinkForm


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
    """删除评论"""
    comment = Comments.objects.get(id=comment_id)
    article_id = comment.article_id
    comment.delete()
    a = request.path
    print(a)
    return redirect('blog:article_comment', article_id=article_id)


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


def friendlink(request):
    """友链"""
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


def delete_friends(request, friends_id):
    link = Friends.objects.get(id=friends_id)
    link.delete()
    return redirect('blog:link_list')
