from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from MyBlog.models import Post

def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'Blog/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'Blog/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post

"""
class PostCreateView(CreateView):
    model = Post
"""


def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})

