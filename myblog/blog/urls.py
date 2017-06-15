from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'^posts/$', views.year_archive, name='archive'),
    url(r'about/$', views.about, name='about'),
]
