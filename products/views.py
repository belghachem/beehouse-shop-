from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def prodects_page(request):
    return render(request, 'products/prodect_page.html')