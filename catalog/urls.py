from django.urls import path

from .views import (ContactsView, ProductCreateView, ProductDetailView,
                    ProductListView, ProductAdminView, ProductUpdateView, ProductDeleteView, ProductStatusToggleView, ProductCategoryListView)

app_name = "catalog"

urlpatterns = [
    path("home/", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("adding_product/", ProductCreateView.as_view(), name="adding_product"),
    path("catalog_admin_page/", ProductAdminView.as_view(), name="catalog_admin_page"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("catalog_admin_page/<int:pk>/", ProductStatusToggleView.as_view(), name="toggle_status"),
    path("products/", ProductCategoryListView.as_view(), name="search"),
]
