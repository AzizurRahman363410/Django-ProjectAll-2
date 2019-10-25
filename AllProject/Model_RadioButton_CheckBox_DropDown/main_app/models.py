from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    fruit = models.CharField(max_length=100)
    media_choice = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    class Meta:
      
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title