from django.contrib import admin

# Register your models here.
from myapp.models import Product


# admin.site.register(Product)

# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category_name')
    ordering = ['category_name']

    # def view_category_link(self, obj):
    #     url = reverse('admin:')


admin.site.register(Product, ProductAdmin)
=======
from myapp.models import Products

admin.site.register(Products)
>>>>>>> origin/main
