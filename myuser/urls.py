from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
                  url(r'^login/$', views.user_login, name='login'),
                  url(r'^logout/$', views.user_logout, name='logout'),
                  url(r'^register/$', views.user_register, name='register'),
                  url(r'^profile/(?P<user_id>\d+)$', views.profile, name='profile'),
                  url(r'^avatar/(?P<user_id>\d+)$', views.change_avatar, name='change_avatar'),
                  # 私信
                  url(r'^post_private/(?P<receiver_id>\d+)/$', views.send_messages, name='send_private'),
                  # 用户管理
                  url(r'^userlist/$', views.userlist, name='userlist'),
                  url(r'^disable/(?P<user_id>\d+)/$', views.disabled_user, name='disable'),
                  url(r'^able/(?P<user_id>\d+)/$', views.abled_user, name='able'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
