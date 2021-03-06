from django.contrib import admin
from .models import Item, Customer, Order, Category, Profile, OrderItem

# Register your models here.
admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(OrderItem)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'image']
