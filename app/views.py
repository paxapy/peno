from django.views.generic.list import ListView

from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'