from django.shortcuts import render
from django.http import HttpResponse

from MyBlog.models import Post


def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'Blog/index.html', context)

def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})

