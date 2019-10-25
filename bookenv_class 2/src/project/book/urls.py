
from django.urls import path
from . import views
urlpatterns = [

    path('',views.HomePageView.as_view(), name='home'),
    path('details/<int:pk>/', views.BookDetailView.as_view(), name='details'), #must give <int:pk> without it class based view will not work.

]