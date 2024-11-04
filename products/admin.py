from django.contrib import admin

from products.models import Basket, Product, ProductCategory

# Register your models here.
admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'stripe_product_price_id')
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'category', 'stripe_product_price_id')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('-name',)

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('products', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0