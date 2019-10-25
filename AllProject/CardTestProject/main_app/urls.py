from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<slug:slug>/', views.DetailView.as_view(), name='detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-summary', views.OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug:slug>/',views.add_to_cart, name='add-to-cart'),
    path('remove-form-cart/<slug:slug>/',views.remove_from_cart, name='remove-form-cart'),
    path('remove-item-from-cart/<slug:slug>/',views.remove_single_item_from_cart, name='remove-single-item-from-cart'),
]
