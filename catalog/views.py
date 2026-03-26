from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def home_page(request):
    products = Product.objects.all()[:6]
    return render(request, "catalog/home.html", {'products': products})


def contacts_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "catalog/contacts.html")
