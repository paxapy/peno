from django.views.generic import list, detail

from .models import Post


class PostList(list.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'


class PostDetail(detail.DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'