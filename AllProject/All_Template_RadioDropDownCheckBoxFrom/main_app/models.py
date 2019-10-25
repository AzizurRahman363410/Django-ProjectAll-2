from django.db import models

# Create your models here.
class Post(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)
    dropdown = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    sports = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
