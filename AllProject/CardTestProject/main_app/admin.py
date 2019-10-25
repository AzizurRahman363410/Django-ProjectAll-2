from django.contrib import admin
from .models import Item, OrderItem, Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', ]
    list_filter = ['ordered', ]


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price',
                    'discount_price', 'description', 'category', 'image']
    list_filter = ['price', ]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
