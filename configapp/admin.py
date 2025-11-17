from django.contrib import admin
from .models import Category, Supplier, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('category_id', 'category_name')
  search_fields = ('category_name',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
  list_display = ('supplier_id', 'company_name', 'contact_name', 'phone')
  search_fields = ('company_name', 'contact_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = (
    'product_id',
    'product_name',
    'supplier',
    'category',
    'unit_price',
    'units_in_stock',
    'discontinued'
  )
  list_filter = ('category', 'supplier', 'discontinued')
  search_fields = ('product_name',)