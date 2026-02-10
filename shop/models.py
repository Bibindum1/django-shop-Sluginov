from django.db import models
from django.db.models import BooleanField


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название категории")
    slug = models.SlugField(max_length=200, verbose_name="Название категории")
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Meta:
    verbose_name = "Категория"
    verbose_name_plural = "Категории"


def __str__(self):
    return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    slug = models.SlugField(max_length=200, verbose_name="Название продукта")
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0, null=True, blank=True)
    is_active: BooleanField = models.BooleanField(default=True, verbose_name="Активно")
    #image = models.ImageField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


updated_at = models.DateTimeField(auto_now=True)


class Meta:
    verbose_name = "Продукт"
    verbose_name_plural = "Продукты"


def __str__(self):
    return f"{self.name}"
