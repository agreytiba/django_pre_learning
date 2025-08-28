from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk','name','description', 'price')   # columns to display in list view
    search_fields = ('name', 'description')  # search box
    list_filter = ('price',) 
    list_editable = ('price',)
    list_per_page = 10

          # filter sidebar
