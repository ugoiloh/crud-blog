from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-id')

class BlogDetailView(DetailView): 
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'
    http_method_names = ['get']

