from django.contrib import admin
from .models import Category, Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','status']
    list_filter = ['category','status']
    search_fields = ['title','description']

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
