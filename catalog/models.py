from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="product_photos/")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Продукт {self.name} из категории {self.category}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['-created_date']


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"Категория {self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']


class Contacts(models.Model):
    country = models.CharField(max_length=50)
    TIN = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Контакты"
        ordering = ['-created_date']
