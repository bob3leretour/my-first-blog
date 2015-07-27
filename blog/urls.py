from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_main),
    url(r'^post/(?P<pk>[0-9]+)/list/$', views.post_list, name='post_list'),
    url(r'^post/contact/$', views.post_contact, name='post_contact'),
    url(r'^post/register/$', views.post_register, name='post_register'),
    url(r'^post/logout/$', views.post_logout, name='post_logout'),
    url(r'^post/login/$', views.post_login, name='post_login'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_details),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)