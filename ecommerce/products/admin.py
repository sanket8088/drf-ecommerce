from django.contrib import admin

from products.models import Categories, Product

# Register your models here.

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['id', 'category_name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['id', 'name' , 'amount']