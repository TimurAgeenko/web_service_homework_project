from django.urls import path
from blog.views import BlogPostListView

app_name = "blog"

urlpatterns = [
    path('blog_home/', BlogPostListView.as_view(), name='blog_home'),
]