from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
                  url(r'^login/$', views.user_login, name='login'),
                  url(r'^logout/$', views.user_logout, name='logout'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
