from django.urls import path
from . import views
app_name = 'main_app'
urlpatterns = [
    path('',views.home, name='home'),
    path('formOne/',views.formOne, name='formOne'),
    path('formTwo/',views.formTwo, name='formTwo'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),

]
