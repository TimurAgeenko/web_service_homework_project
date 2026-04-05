from django.urls import path
from . import views
from .views import ProductListView, ContactsView, ProductDetailView

app_name = "catalog"

urlpatterns = [
    path("home/", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("adding_product/", views.adding_product_page, name="adding"),
]
