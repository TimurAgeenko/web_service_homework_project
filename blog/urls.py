from django.urls import path
from blog.views import BlogPostListView, BlogPostCreateView, BlogPostAdminView

app_name = "blog"

urlpatterns = [
    path('blog_home/', BlogPostListView.as_view(), name='blog_home'),
    path('adding_blog_post/', BlogPostCreateView.as_view(), name='adding_blog_post'),
    path('admin_page/', BlogPostAdminView.as_view(), name='admin_page'),
]