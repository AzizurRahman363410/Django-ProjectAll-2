from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.
SIZE_CHOICE ={
    ('m','M'),
    ('l','L'),
    ('xl','XL'),
    ('fs','FS'),
    ('s','S'),
}

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='picture/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    fabric_origin = models.CharField(max_length=100)
    made_in = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=100, choices=SIZE_CHOICE, default='m')
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

  
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True,)
    phone = models.CharField(max_length=15)
    def __str__(self):
        return self.phone
    
