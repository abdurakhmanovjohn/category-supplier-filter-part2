from django.shortcuts import render, redirect
from .models import Category, Supplier, Product
from .forms import ProductForm

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

def add_product(request):
  if request.method == "POST":
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('index')
  
  else:
    form = ProductForm()
  
  return render(request, 'add_product.html', {'form': form})



