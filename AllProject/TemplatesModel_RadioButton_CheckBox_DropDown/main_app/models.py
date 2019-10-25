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
FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]       
class NewPost(models.Model):
    title = models.CharField(max_length=100)
    n_fruit = models.CharField(max_length=100,choices=FRUIT_CHOICES)
    class Meta:
        verbose_name = 'NewPost'
        verbose_name_plural = 'NewPosts'

    def __str__(self):
        return self.title