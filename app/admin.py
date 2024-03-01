from django.contrib import admin
from .models import Author, BlogPost, Tag

admin.site.register(Author)
admin.site.register(BlogPost)
admin.site.register(Tag)