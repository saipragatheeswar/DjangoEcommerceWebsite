from django.contrib import admin
from .models import Product, Category, Cart, Favourite

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)