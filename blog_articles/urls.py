from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
                  url(r'^$', views.IndexView.as_view(), name='index'),
                  url(r'^aboutme$', views.aboutme, name='aboutme'),
                  url(r'^article/(?P<article_id>\d+)$',
                      views.ArticleDetailView.as_view(), name='detail'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
