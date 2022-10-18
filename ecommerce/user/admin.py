from django.contrib import admin
from user.models import User, Address

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ['id', 'email', 'first_name']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
  list_display = ['id', 'user', 'address']
