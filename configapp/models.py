from django.db import models
from django import forms
import re


class Category(models.Model):
  category_id = models.AutoField(primary_key=True)
  category_name = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  picture = models.ImageField(upload_to='category_pics/', blank=True, null=True)

  def __str__(self):
    return self.category_name
  
  class Meta:
    verbose_name = "Category"
    verbose_name_plural = "Categories"
    # ordering = ['-created_ed']


class Supplier(models.Model):
  supplier_id = models.AutoField(primary_key=True)
  company_name = models.CharField(max_length=150)
  contact_name = models.CharField(max_length=100, blank=True, null=True)
  contact_title = models.CharField(max_length=100, blank=True, null=True)
  address = models.CharField(max_length=200, blank=True, null=True)
  city = models.CharField(max_length=100, blank=True, null=True)
  region = models.CharField(max_length=100, blank=True, null=True)
  postal_code = models.CharField(max_length=20, blank=True, null=True)
  country = models.CharField(max_length=100, blank=True, null=True)
  phone = models.CharField(max_length=30, blank=True, null=True)
  fax = models.CharField(max_length=30, blank=True, null=True)
  homepage = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.company_name
  
  class Meta:
    verbose_name = "Supplier"
    verbose_name_plural = "Suppliers"
    # ordering = ['-created_ed']


class Product(models.Model):
  product_id = models.AutoField(primary_key=True)
  product_name = models.CharField(max_length=150)

  supplier = models.ForeignKey(
    Supplier,
    on_delete=models.CASCADE,
    related_name='products'
  )

  category = models.ForeignKey(
    Category,
    on_delete=models.SET_NULL,
    null=True,
    related_name='products'
  )

  quantity_per_unit = models.CharField(max_length=100, blank=True, null=True)
  unit_price = models.DecimalField(max_digits=10, decimal_places=2)
  units_in_stock = models.IntegerField(default=0)
  units_on_order = models.IntegerField(default=0)
  reorder_level = models.IntegerField(default=0)
  discontinued = models.BooleanField(default=False)

  def __str__(self):
    return self.product_name
  
  class Meta:
    verbose_name = "Product"
    verbose_name_plural = "Products"


class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = '__all__'
    widgets = {
      'product_name': forms.TextInput(attrs={'class': 'form-control'}),
      'supplier': forms.Select(attrs={'class': 'form-control'}),
      'category': forms.Select(attrs={'class': 'form-control'}),
    }
  
  def clean_name(self):
    name = self.cleaned_data['product_name']

    if re.match(r'\d', name):
      raise Exception("Product Name cannot be all Integer")
    
    return name