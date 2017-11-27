from django.conf.urls import url
from posts import views

app_name = 'posts'

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^by/(?P<username>[-\w]+)/(?P<slug>[-\w]+)/$', views.PostDetail.as_view(), name='single'),
]
