from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'popular', ]
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['popular', ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'stock', 'available', 'created', 'updated', 'popular', ]
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['price', 'stock', 'available', 'popular', ]
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
