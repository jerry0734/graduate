from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views, rss
from . import manage_views as manage

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^aboutme$', views.aboutme, name='aboutme'),
    url(r'^categories$', views.showcategories, name='categories'),
    url(r'^categories/(?P<category_id>\d+)$',
        views.CategoryView.as_view(), name='category'),
    # 文章详情
    url(r'^article/(?P<article_id>\d+)$',
        views.detail, name='detail'),
    url(r'^tag/(?P<tag_id>\d+)$', views.Tagview.as_view(), name='tag'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',
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
    # 下面是管理后台的
    url(r'^myarticles/', views.myarticles, name='myarticles'),
    url(r'^delete_article/(?P<article_id>\d+)/$', views.delete_article, name='delete_article'),
    url(r'^article_comment/(?P<article_id>\d+)/$', views.article_comment, name='article_comment'),
    url(r'^manage_comment/edit/(?P<comment_id>\d+)/$', manage.edit_comment, name='manage_c_edit'),
    url(r'^manage_comment/delete/(?P<comment_id>\d+)/$', manage.delete_comment, name='manage_c_del'),
    url(r'^new_article/$', views.new_article, name='new_article'),
    url(r'^edit_article/(?P<article_id>\d+)$',
        views.edit_article, name='edit_article'),
    url(r'^management/$', views.management_index, name='management'),
    url(r'^category_list/$', views.manage_category, name='category_list'),
    url(r'^tag_list/$', views.manage_tags, name='tag_list'),
    url(r'^edit_category/(?P<category_id>\d+)', views.edit_category, name='edit_category'),
    url(r'^edit_tag/(?P<tag_id>\d+)', views.edit_tag, name='edit_tag'),
    url(r'^delete_category/(?P<category_id>\d+)', views.delete_category, name='delete_category'),
    url(r'^delete_tag/(?P<tag_id>\d+)', views.delete_tag, name='delete_tag'),
    # 友链
    url(r'^link_list/$', manage.friendlink, name='link_list'),
    url(r'^delete_link/(?P<friends_id>\d+)/$', manage.delete_friends, name='del_link'),
    # 修改关于博客
    url(r'^manage_aboutme/(?P<id>\d+)$', manage.edit_aboutme, name='edit_aboutme'),
    # rss
    url(r'^latest/feed/$', rss.LatestArticle(), name='rss'),
]
