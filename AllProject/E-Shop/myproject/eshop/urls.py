from django.urls import path
from . import views

app_name='eshop'
urlpatterns = [
    path('', views.home, name='home'),
    path('product_list/', views.productList, name='product'),
    path('detail/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('checkout/', views.checkout, name='checkout'),
   
]
