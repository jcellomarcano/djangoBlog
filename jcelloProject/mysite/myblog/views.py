from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
# Create your views here.

class PostList(ListView):
    """docstring for [object Object]."""
    model = Post
    template_name = 'post_list.html'
    paginate_by = 6
    context_object_name = "post_list"

    def get_quieryset(self, **kwargs):
        return Post.objects.filter(presentar = True).order_by("-publicado")

class PostDetailView(DetailView):
    """docstring for [object Object]."""
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context
