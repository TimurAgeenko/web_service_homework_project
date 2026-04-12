from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from blog.forms import BlogPostForm
from blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'
    template_name = 'blog/blog_home.html'
    paginate_by = 6

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


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
    template_name = 'blog/blog_admin_page.html'
    paginate_by = 20


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    context_object_name = 'blog_post'
    template_name = 'blog/adding_blog_post.html'

    def get_success_url(self):
        return reverse('blog:blog_post_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    context_object_name = 'blog_post'
    template_name = 'blog/blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog:admin_page')


class BlogPostDetailView(DetailView):
    model = BlogPost
    context_object_name = 'blog_post'
    template_name = 'blog/blog_post_detail.html'
    views = model.views

    def get_object(self, queryset=None):
        item = super().get_object(queryset)
        item.views += 1
        item.save()

        if item.views == 100:
            send_mail(
                subject=f'Популярная статья: {item.title}',
                message=f'Статья {item.title} набрала 100 просмотров!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['ageenko.timur.10@gmail.com'],
                fail_silently=True,
            )

        return item


class BlogPostStatusToggleView(View):
    context_object_name = 'post'
    template_name = 'blog/blog_admin_page.html'

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(BlogPost, pk=kwargs['pk'])
        post.is_published = not post.is_published
        post.save()
        return redirect('blog:admin_page')
