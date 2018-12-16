from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def post_list(request):
    posts = Post.objects.order_by('created')
    categories = Category.objects.order_by('name')
    return render(request, 'blog/post_list.html', {'newest': posts[0], 'posts': posts[1:], 'categories': categories})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = Category.objects.order_by('name')
    return render(request, 'blog/post_detail.html', {'post': post, 'categories': categories})
