from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import PostForm
from django.utils import timezone


def post_list(request):
    posts = Post.objects.order_by('created')
    categories = Category.objects.order_by('name')
    return render(request, 'blog/post_list.html', {'newest': posts[0], 'posts': posts[1:], 'categories': categories})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = Category.objects.order_by('name')
    if request.method == 'POST':
        return redirect('post_edit', pk=post.pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'categories': categories})


def post_list_filtered_by_category(request, category):
    c = get_object_or_404(Category, name=category)
    posts = Post.objects.filter(category=c).order_by('created')
    categories = Category.objects.order_by('name')
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})



