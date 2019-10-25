from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug>/', views.detail, name='detail'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('send_mail/', views.send_email, name='send_mail'),
   
]
