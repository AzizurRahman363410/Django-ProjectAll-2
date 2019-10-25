
from django.urls import path
from . import views
app_name='book'
urlpatterns = [

    path('',views.HomePageView.as_view(), name='home'),
    path('details/<int:pk>/', views.BookDetailView.as_view(), name='details'), #must give <int:pk> without it class based view will not work.
    path('search/',views.search, name='search'),
    path('create/',views.BookCreateView.as_view(), name='create'),
    path('create/<int:pk>/',views.BookUpdateView.as_view(), name='update'),
]