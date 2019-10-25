from django.contrib import admin
from . models import Product,Profile
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','image','price','description','fabric_origin','made_in','color','size','pub_date')
    list_display_links = ['title','image']
    list_editable = ['price','color','size',]
    list_filter = ['title','made_in','size','pub_date',]
    prepopulated_fields = {'slug': ('title',)}
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','phone',)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile,ProfileAdmin)
