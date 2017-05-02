"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from . import settings

urlpatterns = [
                  # 引用blog_articles里面的urls.py
                  url(r'', include('blog_articles.urls', namespace='blog')),
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^draceditor/', include('draceditor.urls')),
                  url(r'^board/', include('msb.urls', namespace='msb')),
                  url(r'^account/', include('myuser.urls', namespace='account')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
