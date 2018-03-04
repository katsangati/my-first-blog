from django.conf.urls import url
from . import views

# only an empty string will match this pattern
# it will tell Django that views.post_list is the right place to go if someone enters your website
# at the 'http://127.0.0.1:8000/' address.

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
