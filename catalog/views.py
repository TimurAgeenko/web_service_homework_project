from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, FormView, ListView, UpdateView, DeleteView, View

from .forms import ContactForm, ProductForm
from .models import Contacts, Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/home.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class ContactsView(FormView):
    form_class = ContactForm
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:contacts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.order_by('-id').first()
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']

        messages.success(self.request, f'Спасибо, {name}! Ваше сообщение получено.')

        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'catalog/product.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'catalog/adding_product.html'
    success_url = reverse_lazy('catalog:adding_product')

    def form_valid(self, form):
        form.instance.owner = self.request.user

        messages.success(self.request, 'Товар успешно добавлен!')

        return super().form_valid(form)


class ProductAdminView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/catalog_admin_page.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.groups.filter(name='Модератор продуктов').exists() or self.request.user.is_superuser:
            return Product.objects.all()
        return Product.objects.filter(owner=self.request.user)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'catalog/adding_product.html'
    success_url = reverse_lazy('catalog:catalog_admin_page')

    def test_func(self):
        product = self.get_object()
        return self.request.user.is_superuser or self.request.user == product.owner



class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog_admin_page')

    def test_func(self):
        product = self.get_object()
        user = self.request.user

        is_owner = product.owner == user
        is_moderator = (
            user.groups.filter(name="Модератор продуктов").exists()
            and user.has_perm('catalog.delete_product')
        )

        return user.is_superuser or is_owner or is_moderator


class ProductStatusToggleView(LoginRequiredMixin, PermissionRequiredMixin, View):
    context_object_name = 'product'
    template_name = 'catalog/catalog_admin_page.html'
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        product.is_published = not product.is_published
        product.save()
        return redirect("catalog:catalog_admin_page")