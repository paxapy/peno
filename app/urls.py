from django.conf.urls import patterns, url

from .views import PostList

urlpatterns = patterns(
    '',
    url(r'^$', PostList.as_view()),
)
