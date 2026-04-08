from django.urls import path

from .views import (ContactsView, ProductCreateView, ProductDetailView,
                    ProductListView, ProductAdminView, ProductUpdateView)

app_name = "catalog"

urlpatterns = [
    path("home/", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("adding_product/", ProductCreateView.as_view(), name="adding"),
    path("catalog_admin_page/", ProductAdminView.as_view(), name="catalog_admin_page"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
]
