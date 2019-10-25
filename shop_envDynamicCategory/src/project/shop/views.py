from django.shortcuts import render,get_object_or_404
from . models import Product,Category,Sub_Category
# Create your views here.
def product_list(request, category_slug=None):
    category = None

    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    # sub_sategory = Sub_Category.objects.all()

    if category_slug:
        category =get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'categories':categories,
        'category':category,
        # 'sub_sategory':sub_sategory,
        'products':products
    }
    return render(request, 'shop/product_list.html',context)