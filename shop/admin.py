from django.contrib import admin
from .models import Product
from django.contrib import admin
from django.contrib.auth.models import User, Group
from shop.models import Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk','name','description', 'price')   # columns to display in list view
    search_fields = ('name', 'description')  # search box
    list_filter = ('price',) 
    list_editable = ('price',)
    list_per_page = 10


from django.contrib import admin
from django.contrib.auth.models import User, Group
from shop.models import Product  # make sure you have a Product model

class CustomAdminSite(admin.AdminSite):
    site_header = "💙 My Custom Admin"
    site_title = "Custom Admin"
    index_title = "Dashboard"

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['user_count'] = User.objects.count()
        extra_context['group_count'] = Group.objects.count()
        extra_context['product_count'] = Product.objects.count()
        return super().index(request, extra_context=extra_context)

# Create an instance
custom_admin_site = CustomAdminSite(name='custom_admin')

# Register models with the custom admin
custom_admin_site.register(User)
custom_admin_site.register(Group)
custom_admin_site.register(Product)
