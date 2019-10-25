from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('create_product/', views.create_product, name='create_product'),
    path('search/', views.search, name='search'),
    path('delete/<int:pk>/', views.BlogDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='update'),

]
