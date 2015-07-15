from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^caca$', views.post_list),

    url(r'^post/register/$', views.post_register, name='post_register'),
    url(r'^post/logout/$', views.post_logout, name='post_logout'),
    url(r'^post/login/$', views.post_login, name='post_login'),
    url(r'^post/(?P<pk>[1-9]+)/$', views.post_details),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
]