from django.urls import path

from .views import (ContactsView, ProductCreateView, ProductDetailView,
                    ProductListView)

app_name = "catalog"

urlpatterns = [
    path("home/", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("adding_product/", ProductCreateView.as_view(), name="adding"),
]
