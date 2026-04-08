from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, ListView, UpdateView

from .forms import ContactForm, ProductForm
from .models import Contacts, Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/home.html'
    paginate_by = 6


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'catalog/adding_product.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно добавлен!')

        return super().form_valid(form)


class ProductAdminView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/catalog_admin_page.html'
    paginate_by = 10


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    template_name = 'catalog/adding_product.html'
    success_url = reverse_lazy('catalog:catalog_admin_page')