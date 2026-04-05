from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm
from .models import Product, Contacts, Category


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


def product_page(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "catalog/product.html", {'product': product})


def adding_product_page(request):
    categories = Category.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        category_id = request.POST.get("category")
        category = Category.objects.get(id=category_id)
        price = request.POST.get("price")
        image = request.FILES.get("image")
        description = request.POST.get("description")

        product = Product.objects.create(name=name, category=category, price=price, image=image, description=description)
        return render(request, "catalog/adding_product.html", {'product': product})
    return render(request, "catalog/adding_product.html", {'categories': categories})
