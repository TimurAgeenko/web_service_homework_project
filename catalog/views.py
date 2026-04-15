from django.contrib import messages
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, FormView, ListView, UpdateView, DeleteView, View

from .forms import ContactForm, ProductForm
from .models import Contacts, Product
from .services import get_products_by_search


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/home.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = cache.get('products_queryset')

        if not queryset:
            queryset = Product.objects.filter(is_published=True)
            cache.set('products_queryset', queryset, 60 * 15)

        return queryset


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


@method_decorator(cache_page(60 * 15), name='dispatch')
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
        if self.request.user.groups.filter(name='Moders').exists() or self.request.user.is_superuser:
            return Product.objects.all()
        return Product.objects.filter(owner=self.request.user)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'catalog/adding_product.html'
    success_url = reverse_lazy('catalog:catalog_admin_page')


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog_admin_page')


class ProductStatusToggleView(PermissionRequiredMixin, View):
    context_object_name = 'product'
    template_name = 'catalog/catalog_admin_page.html'
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        product.is_published = not product.is_published
        product.save()
        return redirect("catalog:catalog_admin_page")


class ProductCategoryListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/products_by_category.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('search')

        return get_products_by_search(queryset, query)
