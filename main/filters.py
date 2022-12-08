from django_filters.rest_framework import FilterSet
import django_filters

from .models import Product

class ProductFilter(FilterSet):
    category_title = django_filters.CharFilter(field_name='category__title')
    category_id = django_filters.NumberFilter(field_name='category') 

    class Meta:
        model = Product
        fields = ['category_title','category_id','status']