from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, "catalog/home.html")


def contacts_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "catalog/contacts.html")
