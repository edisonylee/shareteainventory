from django.shortcuts import render
from .models import BobaProduct

def list_boba_products(request):
    products = BobaProduct.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

# Create your views here.
