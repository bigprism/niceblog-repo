from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog_post/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('blog_post/create/', views.blog_post_create, name='blog_post_create'),
    path('blog_post/<int:pk>/update/', views.blog_post_update, name='blog_post_update'),
    path('blog_post/<int:pk>/delete/', views.blog_post_delete, name='blog_post_delete'),

    path('api/blog_post/create/', views.create_blog_post, name='create_blog_post'),
    path('api/blog_post/<int:pk>/', views.get_blog_post, name='get_blog_post'),
    path('api/blog_post/<int:pk>/update/', views.update_blog_post, name='update_blog_post'),
    path('api/blog_post/<int:pk>/delete/', views.delete_blog_post, name='delete_blog_post'),
]