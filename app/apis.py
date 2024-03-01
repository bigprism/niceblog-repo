from django.http import JsonResponse

from .models import BlogPost


def create_blog_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        tags = request.POST.getlist('tags')

        blog_post = BlogPost.objects.create(title=title, content=content, author_id=author)
        blog_post.tags.set(tags)

        return JsonResponse({'success': True, 'blog_post_id': blog_post.id})
    else:
        return JsonResponse({'success': False})


def get_blog_post(request, pk):
    try:
        blog_post = BlogPost.objects.get(pk=pk)
        return JsonResponse({
            'success': True,
            'title': blog_post.title,
            'content': blog_post.content,
            'author': blog_post.author.username,
            'tags': [tag.name for tag in blog_post.tags.all()]
        })
    except BlogPost.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Blog post not found'})


def update_blog_post(request, pk):
    if request.method == 'PUT':
        try:
            blog_post = BlogPost.objects.get(pk=pk)
            title = request.PUT.get('title')
            content = request.PUT.get('content')
            author = request.PUT.get('author')
            tags = request.PUT.getlist('tags')

            blog_post.title = title
            blog_post.content = content
            blog_post.author_id = author
            blog_post.tags.set(tags)
            blog_post.save()

            return JsonResponse({'success': True})
        except BlogPost.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Blog post not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


def delete_blog_post(request, pk):
    try:
        blog_post = BlogPost.objects.get(pk=pk)
        blog_post.delete()
        return JsonResponse({'success': True})
    except BlogPost.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Blog post not found'})