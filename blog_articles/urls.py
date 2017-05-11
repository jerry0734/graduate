from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^aboutme$', views.aboutme, name='aboutme'),
    url(r'^categories$', views.showcategories, name='categories'),
    url(r'^categories/(?P<category_id>\d+)$',
        views.CategoryView.as_view(), name='category'),
    # 文章详情
    url(r'^article/(?P<article_id>\d+)$',
        views.ArticleDetailView.as_view(), name='detail'),
    url(r'^tag/(?P<tag_id>\d+)$', views.Tagview.as_view(), name='tag'),
    url(r'^archives/(?P<year>[0-9]{4})/$',
        views.archive, name='archive'),
    # 写评论
    url(r'^article/(?P<article_id>\d+)/comment/$',
        views.write_comments, name='comment'),
    # 删除评论
    url(r'^delete_comment/(?P<comment_id>\d+)/$',
        views.delete_comment, name='delete_comment'),
    url(r'^edit_comment/(?P<comment_id>\d+)/$',
        views.edit_comment, name='edit_comment'),
    url(r'^search/$', views.search_article, name='search'),
    url(r'^new_article/$', views.new_article, name='new_article'),
    url(r'^edit_article/(?P<article_id>\d+)$',
        views.edit_article, name='edit_article'),
    url(r'^management/$', views.management_index, name='management'),
    url(r'^category_list/$', views.manage_category, name='category_list'),
    url(r'^tag_list/$', views.manage_tags, name='tag_list'),
]
