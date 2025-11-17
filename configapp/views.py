from django.shortcuts import render
from .models import Category, Supplier, Product

def index(request):
  categories = Category.objects.all()
  suppliers = Supplier.objects.all()

  selected_category = request.GET.get('category')
  selected_supplier = request.GET.get('supplier')

  products = Product.objects.all()

  if selected_category:
    products = products.filter(category_id=selected_category)

  if selected_supplier:
    products = products.filter(supplier_id=selected_supplier)

  context = {
    'categories': categories,
    'suppliers': suppliers,
    'products': products,
    'selected_category': selected_category,
    'selected_supplier': selected_supplier,
  }

  return render(request, 'index.html', context)



