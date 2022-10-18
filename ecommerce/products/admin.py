from django.contrib import admin

from products.models import Categories

# Register your models here.

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['id', 'category_name']