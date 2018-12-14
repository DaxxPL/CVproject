from django.shortcuts import render
from .models import Post, Category


def post_list(request):
    posts = Post.objects.order_by('created')
    categories = Category.objects.order_by('name')
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})
