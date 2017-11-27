from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.


class PostDetail(generic.DetailView):
    model = Post
    select_related = ('user', 'category')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


