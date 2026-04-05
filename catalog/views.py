from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Product, Contacts, Category


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/home.html'
    paginate_by = 6


def contacts_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    contacts = Contacts.objects.all()[0]
    return render(request, "catalog/contacts.html", {'contacts': contacts})


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
