from django.conf.urls import url
from category import views

app_name = 'categories'

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^posts/in/(?P<slug>[-\w]+)/$', views.SingleGroup.as_view(), name='single'),
]
