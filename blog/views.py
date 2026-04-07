from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from blog.forms import BlogPostForm
from blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'
    template_name = 'blog/blog_home.html'
    paginate_by = 6


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    context_object_name = 'blog_post'
    template_name = 'blog/adding_blog_post.html'
    success_url = reverse_lazy('blog:adding_blog_post')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно добавлен!')

        return super().form_valid(form)


class BlogPostAdminView(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'
    template_name = 'blog/admin_page.html'
    paginate_by = 20


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    context_object_name = 'blog_post'
    template_name = 'blog/adding_blog_post.html'
    success_url = reverse_lazy('blog:admin_page')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog:blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog:admin_page')
