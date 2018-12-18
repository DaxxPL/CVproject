from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from .forms import PostForm
from django.utils import timezone
from django.core.paginator import Paginator


def post_list(request):
    categories = Category.objects.order_by('name')
    if request.method == 'GET':
        if 'category' in request.GET.keys():
                posts = Post.objects.order_by('-created').\
                    filter(category=Category.objects.filter(name=request.GET['category']).first())
                paginator = Paginator(posts, 9)
                page = request.GET.get('page')
                paged_posts = paginator.get_page(page)
                return render(request, 'blog/post_list.html', {'posts': paged_posts,
                                                               'rest': paged_posts,
                                                               'categories': categories,
                                                               'category': request.GET['category']})
        else:
            posts = Post.objects.order_by('-created')
            paginator = Paginator(posts, 9)
            page = request.GET.get('page')
            paged_posts = paginator.get_page(page)
            if page in [None, '1']:
                return render(request, 'blog/post_list.html', {'posts': paged_posts,
                                                               'first': paged_posts[0],
                                                               'rest': paged_posts[1:],
                                                               'categories': categories})
            return render(request, 'blog/post_list.html', {'posts': paged_posts,
                                                           'rest': paged_posts,
                                                           'categories': categories})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = Category.objects.order_by('name')
    if request.method == 'POST':
        if request.POST['button'] == 'edit':
            return redirect('post_edit', pk=post.pk)
        elif request.POST['button'] == 'delete':
            post.delete()
            return redirect('post_list')
    return render(request, 'blog/post_detail.html', {'post': post, 'categories': categories})


@login_required
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


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
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



