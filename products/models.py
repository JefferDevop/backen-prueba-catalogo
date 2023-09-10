from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# from simple_history.models import HistoricalRecords
from cloudinary.models import CloudinaryField
from django_tenants.utils import get_public_schema_name
from django.conf import settings
from requests import request

global_schema_name = None

from django.shortcuts import render


class Product(models.Model):
    codigo = models.BigAutoField(
        primary_key=True, auto_created=True, verbose_name=("Código")
    )
    name_extend = models.CharField(
        max_length=200, unique=True, verbose_name=("Nombre Producto")
    )

    images = CloudinaryField(
        "categories/",
        blank=True,
        transformation=[
            {"width": 800, "height": 1200, "crop": "limit"},
            {"quality": "auto"},
        ],
        format="webp",
    )
    description = models.TextField(
        max_length=4000, blank=True, verbose_name=("Descripción el producto")
    )
    price1 = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=("Precio Detal")
    )
    price2 = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=("Precio por Mayor")
    )
    price_old = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=("Precio Anterior")
    )
    flag = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=("Grupo")
    )
    ref = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=("Referencia")
    )
    slug = models.SlugField(max_length=200, unique=True, verbose_name=("Url"))
    active = models.BooleanField(default=True, verbose_name=("Activo"))
    soldout = models.BooleanField(default=False, verbose_name=("Agotado"))
    offer = models.BooleanField(default=False, verbose_name=("Oferta"))
    home = models.BooleanField(default=False, verbose_name=("Exclusivo"))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=("Creado"))
    modified_date = models.DateTimeField(auto_now=True, verbose_name=("Modificado"))
    # history = HistoricalRecords()

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.name_extend} : cod:{self.codigo}"


class Category(models.Model):
    codigo = models.CharField(max_length=10, unique=True, verbose_name=("Código"))
    name = models.CharField(max_length=50, unique=True, verbose_name=("Nombre"))
    slug = models.SlugField(max_length=100, unique=True, verbose_name=("Url"))
    image_alterna = models.CharField(max_length=600, null=True, blank=True)
    image = CloudinaryField(
        "categories/",
        blank=True,
        transformation=[
            {"width": 800, "height": 800, "crop": "limit"},
            {"quality": "auto"},
        ],
        format="webp",
    )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=("Creado"))
    modified_date = models.DateTimeField(auto_now=True, verbose_name=("Modificado"))
    # history = HistoricalRecords()

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def get_url(self):
        return reverse("products_by_category", args=[self.slug])

    def __str__(self):
        return self.name

class CategoryProduct(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=("Producto")
    )
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=("Creado"))
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name=("Categoría")
    )

    class Meta:
        verbose_name = "Categoria de Producto"
        verbose_name_plural = "Categoria de Productos"

    def __str__(self):
        return str(self.category)

class Gallery(models.Model):
    product = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE, verbose_name=("Producto")
    )
    image = CloudinaryField("gallery", blank=True)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Galeria de Imagenes"

class Attribut(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=("Nombre"))
    # history = HistoricalRecords()

    class Meta:
        verbose_name = "Atributo"
        verbose_name_plural = "Atributos"

    def __str__(self):
        return self.name
