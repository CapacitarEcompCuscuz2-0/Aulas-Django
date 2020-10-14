from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Post


# Create your views here.

class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/postslist.html'

class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/detail.html'

class PostCreateView(generic.CreateView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/create.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('todos')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)