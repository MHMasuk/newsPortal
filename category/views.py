from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Category
from posts.models import Post
# Create your views here.


def Index(request):
    '''
    template_name = 'index.html'
    model = Post

    context_object_name = 'posts'
    '''
    post = Post.objects.all()
    category = Category.objects.all()
    context = {
        'posts': post,
        'categories': category,
    }

    return render(request, 'index.html', context)


class GroupPost(generic.DetailView):
    model = Category


class SingleGroup(generic.DetailView):
    model = Category



