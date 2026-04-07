from django.urls import path
from blog.views import BlogPostListView, BlogPostCreateView, BlogPostAdminView, BlogPostUpdateView, BlogPostDetailView, BlogPostDeleteView

app_name = "blog"

urlpatterns = [
    path('blog_home/', BlogPostListView.as_view(), name='blog_home'),
    path('admin_page/', BlogPostAdminView.as_view(), name='admin_page'),
    path('blog_post/new/', BlogPostCreateView.as_view(), name='adding_blog_post'),
    path('blog_post/<int:pk>/', BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog_post/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blog_post_edit'),
    path('blog_post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blog_post_delete'),
]