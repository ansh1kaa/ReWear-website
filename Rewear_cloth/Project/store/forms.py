from django.contrib import admin
from .models import Category, Product, ProductImage
from .models import Product
from django import forms

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'seller', 'created_at']
    inlines = [ProductImageInline]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'main_image']