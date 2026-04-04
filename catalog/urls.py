from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("home/", views.home_page, name="home"),
    path("contacts/", views.contacts_page, name="contacts"),
    path("products/<int:product_id>/", views.product_page, name="product"),
    path("adding_product/", views.adding_product_page, name="adding"),
]
