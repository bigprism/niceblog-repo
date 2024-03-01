from django.test import TestCase
from .models import BlogPost

class BlogPostCreateTestCase(TestCase):
    def test_create_blog_post(self):
        """
        Test that a blog post can be created.
        """
        data = {
            'title': 'Test Blog Post',
            'content': 'This is a test blog post.',
            'author': 1,
            'tags': [1, 2]
        }
        response = self.client.post('/api/blog_post/create/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(BlogPost.objects.count(), 1)

from django.test import TestCase
from .models import BlogPost

class BlogPostGetTestCase(TestCase):
    def test_get_blog_post(self):
        """
        Test that a blog post can be retrieved.
        """
        blog_post = BlogPost.objects.create(title='Test Blog Post', content='This is a test blog post.', author_id=1)
        response = self.client.get(f'/api/blog_post/{blog_post.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Blog Post')

from django.test import TestCase
from .models import BlogPost

class BlogPostUpdateTestCase(TestCase):
    def test_update_blog_post(self):
        """
        Test that a blog post can be updated.
        """
        blog_post = BlogPost.objects.create(title='Test Blog Post', content='This is a test blog post.', author_id=1)
        data = {
            'title': 'Updated Test Blog Post',
            'content': 'This is an updated test blog post.',
            'author': 1,
            'tags': [1, 2]
        }
        response = self.client.put(f'/api/blog_post/{blog_post.id}/update/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(BlogPost.objects.get(id=blog_post.id).title, 'Updated Test Blog Post')

from django.test import TestCase
from .models import BlogPost

class BlogPostDeleteTestCase(TestCase):
    def test_delete_blog_post(self):
        """
        Test that a blog post can be deleted.
        """
        blog_post = BlogPost.objects.create(title='Test Blog Post', content='This is a test blog post.', author_id=1)
        response = self.client.delete(f'/api/blog_post/{blog_post.id}/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(BlogPost.objects.count(), 0)