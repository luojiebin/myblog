from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'^posts/$', views.year_archive, name='archive'),
    url(r'^tags/(?P<slug>[\w-]+)/$', views.tag_detail, name='tag_detail'),
    url(r'^tags/$', views.tags, name='tags'),
    url(r'about/$', views.about, name='about'),
]
