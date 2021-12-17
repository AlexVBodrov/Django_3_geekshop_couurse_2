from django.contrib import admin
from products.models import ProductCategory, Product

# Register your models here.

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = (('name', 'category'), 'description', 'price', 'quantity', 'image',)
    readonly_fields = ('description',)
    ordering = ('name',)
    search_fields = ('name',)