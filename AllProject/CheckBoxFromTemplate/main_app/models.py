from django.db import models

# Create your models here.
class Post(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email
    