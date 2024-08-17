from django.contrib import admin
from main.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "product_name", "category",)
    list_filter = ("category",)
    search_fields = ("category_name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "category_name",)

