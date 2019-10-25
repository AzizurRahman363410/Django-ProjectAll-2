from django.urls import path
from . import views
app_name ='shop'
urlpatterns = [
    path('',views.HomeListView.as_view(), name='home'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('sale/',views.sale, name='sale'),
     path('detail',views.detail, name='detail'),
]