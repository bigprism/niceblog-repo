from django.contrib.auth.models import User

from django.db import models

from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True)
    featured_image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[str(self.id)])


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name