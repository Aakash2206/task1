from .models import Product
import django_filters
from django import forms


class ProductFilter(django_filters.FilterSet):
    Product_Name = django_filters.CharFilter(lookup_expr='icontains')
    Category = django_filters.ModelMultipleChoiceFilter(
        queryset=Product.objects.values_list('Category', flat=True).distinct(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        fields = ['Product_Id', 'Product_Name', 'Category', ]
