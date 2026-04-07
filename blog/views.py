from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'
    template_name = 'blog/blog_home.html'
    paginate_by = 6
