from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Comment, Post
from django.urls import reverse_lazy


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

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'body']
    success_url = "/"

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog:home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = ['comment']
    success_url = "/"

    def form_valid(self, form): 
        form.instance.blog_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    


