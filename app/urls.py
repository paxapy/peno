from django.conf.urls import patterns, url

from .views import PostList, PostDetail

urlpatterns = patterns(
    '',
    url(r'^$', PostList.as_view()),
    url(r'^news/(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),
)
