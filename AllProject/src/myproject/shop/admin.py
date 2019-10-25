from django.contrib import admin

# Register your models here.
from .models import Item, OrderItem, Order

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title','price','discount_price','category','label','slug','image','description')
    prepopulated_fields ={'slug':('title',)}

admin.site.register(Item,ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)