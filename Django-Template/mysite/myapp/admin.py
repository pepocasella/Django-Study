from django.contrib import admin
from .models import Client, Supplier, Product

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'unit', 'street', 'neighborhood', 'industry']
    list_filter = ['name', 'slug', 'unit', 'street', 'neighborhood', 'industry']
    search_fields = ['name', 'slug', 'unit', 'street']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'street', 'neighborhood', 'phone_number', 'created_at']
    list_filter = ['name', 'slug', 'street', 'neighborhood', 'phone_number', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'image', 'product_slug', 'portal_name', 'category', 'quantity', 'unit_price', 'client', 'supplier', 'created_at', 'updated_at', 'status']
    list_filter = ['product_name', 'image', 'product_slug', 'portal_name', 'category', 'quantity', 'unit_price', 'client', 'supplier', 'created_at', 'updated_at', 'status']
    search_fields = ['product_name', 'product_slug', 'portal_name', 'category', 'quantity', 'unit_price', 'status']
    prepopulated_fields = {'product_slug': ('product_name',)}