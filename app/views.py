from django.shortcuts import render

from .models import BlogPost

from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect

from .forms import BlogPostForm

from django.shortcuts import render, get_object_or_404, redirect

from django.shortcuts import redirect, get_object_or_404


def index(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'index.html', {'blog_posts': blog_posts})


def blog_post_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_post_detail.html', {'blog_post': blog_post})


def blog_post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save()
            return redirect('blog_post_detail', pk=blog_post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog_post_create.html', {'form': form})


def blog_post_update(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blog_post_detail', pk=blog_post.pk)
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'blog_post_update.html', {'form': form, 'blog_post': blog_post})


def blog_post_delete(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    blog_post.delete()
    return redirect('index')