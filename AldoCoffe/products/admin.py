from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
