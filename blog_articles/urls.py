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
    url(r'^article/(?P<article_id>\d+)$',
        views.ArticleDetailView.as_view(), name='detail'),
    url(r'^tag/(?P<tag_id>\d+)$', views.Tagview.as_view(), name='tag'),
    url(r'^archives/(?P<year>[0-9]{4})/$',
        views.archive, name='archive'),
    url(r'^article/(?P<article_id>\d+)/comment/$',
        views.write_comments, name='comment'),
    url(r'^search/$', views.search_article, name='search'),
]
