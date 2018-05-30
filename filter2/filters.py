from .models import Product, Subcat
import django_filters
from django import forms


class ProductFilter(django_filters.FilterSet):
    Product_Name = django_filters.CharFilter(lookup_expr='icontains')
    '''Category = django_filters.ModelMultipleChoiceFilter(
        queryset=Product.objects.values_list('Category', flat=True).distinct(),
        widget=forms.CheckboxSelectMultiple)
    
    Subcategory = Category = django_filters.ModelMultipleChoiceFilter(
        queryset=Subcat.objects.values_list('Subca_Name', flat=True).distinct(),
        widget=forms.CheckboxSelectMultiple)
    '''
    class Meta:
        model = Product
        fields = ['Product_Id', 'Product_Name', 'Category']

'''
class SubFilter(django_filters.FilterSet):
    Subcat_Name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Subcat
        fields = {'Subcat_Name'}
'''