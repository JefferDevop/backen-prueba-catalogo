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
        primary_key=True, auto_created=True, verbose_name=(u'Código'))
    name_extend = models.CharField(max_length=200, unique=True,
                                   verbose_name=(u'Nombre Producto'))    

    images = CloudinaryField('categories/', blank=True,  transformation=[{'width': 800, 'height': 1200, 'crop': 'limit'}, {'quality': 'auto'}], 
                            format='webp')
    description = models.TextField(
        max_length=4000, blank=True, verbose_name=(u'Descripción el producto'))
    price1 = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=(u'Precio Detal'))
    price2 = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=(u'Precio por Mayor')) 
    price_old = models.PositiveIntegerField(
        blank=True, null=True, verbose_name=(u'Precio Anterior'))
    flag = models.CharField(max_length=200, blank=True, null=True,
                            verbose_name=(u'Grupo'))
    
    ref = models.CharField(max_length=200, blank=True, null=True,
                            verbose_name=(u'Referencia'))
    
    slug = models.SlugField(max_length=200, unique=True, verbose_name=(u'Url'))
    
    
    active = models.BooleanField(default=True, verbose_name=(u'Activo'))
    soldout = models.BooleanField(default=False, verbose_name=(u'Agotado'))
    offer = models.BooleanField(default=False, verbose_name=(u'Oferta'))
    home = models.BooleanField(default=False, verbose_name=(u'Exclusivo'))
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name=(u'Creado'))
    modified_date = models.DateTimeField(
        auto_now=True, verbose_name=(u'Modificado'))
    # history = HistoricalRecords()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'{self.name_extend} : cod:{self.codigo}'    

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name=(u'Nombre'))
    slug = models.SlugField(max_length=100, unique=True, verbose_name=(u'Url'))

    image = CloudinaryField('categories/',  blank=True, 
                            transformation=[{'width': 800, 'height': 800, 'crop': 'limit'}, {'quality': 'auto'}], 
                            format='webp')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name=(u'Creado'))
    modified_date = models.DateTimeField(
        auto_now=True, verbose_name=(u'Modificado'))
    # history = HistoricalRecords()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name
    
 
class CategoryProduct(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=(u'Producto'))
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name=(u'Creado'))
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name=(u'Categoría'))

    class Meta:
        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categoria de Productos'

    def __str__(self):
        return str(self.category)


class Gallery(models.Model):
    product = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE, verbose_name=(u'Producto'))
    image = CloudinaryField('gallery', blank=True)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Galeria de Imagenes'


class Attribut(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name=(u'Nombre'))
    # history = HistoricalRecords()

    class Meta:
        verbose_name = 'Atributo'
        verbose_name_plural = 'Atributos'

    def __str__(self):
        return self.name
