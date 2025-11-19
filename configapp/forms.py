from django import forms
import re
from .models import Product

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