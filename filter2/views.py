from django.contrib.auth.models import User
from django.shortcuts import render

from filter2.models import Product
from .filters import ProductFilter


def search(request):
    product_list = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, 'filter2/product_list.html', {'filter': product_filter})
