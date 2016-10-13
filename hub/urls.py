from django.conf.urls import url

from .views import ArtListView, ArtDetailView


urlpatterns = [
    url('^$', ArtListView.as_view(), name='index'),
    url('^category/(?P<category>[-\w]+)/$', ArtListView.as_view(), name='category'),
    url('^art/(?P<slug>[-\w]+)/$', ArtDetailView.as_view(), name='art_detail')
]
