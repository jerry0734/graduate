from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
                  url(r'^$', views.MessageBoard, name='board'),
                  url(r'^manage/$', views.msb_manage, name='manage'),
                  url(r'^delete/(?P<message_id>\d+)/$', views.msb_manage, name='delete'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
