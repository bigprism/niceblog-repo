from django.urls import path
from . import views

urlpatterns = [
    path('api/blog_post/create/', views.create_blog_post, name='create_blog_post'),
    path('api/blog_post/<int:pk>/', views.get_blog_post, name='get_blog_post'),
    path('api/blog_post/<int:pk>/update/', views.update_blog_post, name='update_blog_post'),
    path('api/blog_post/<int:pk>/delete/', views.delete_blog_post, name='delete_blog_post'),
]