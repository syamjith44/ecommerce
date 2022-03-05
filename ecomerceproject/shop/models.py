from distutils.command.upload import upload

from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    popular = models.BooleanField(default=False, )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('shop:allProductCategory', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.title)


class Product(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True, )
    popular = models.BooleanField(default=False, )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_url(self):
        return reverse('shop:allProductCategory', args=[self.slug])

    def get_product_url(self):
        return reverse('shop:productDetail', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.title)


class Offers(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    available = models.BooleanField(default=False, )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'

    def __str__(self):
        return '{}'.format(self.title)
