from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    desc = models.TextField()
    publisher =models.CharField(max_length=100)
    image = models.ImageField(upload_to='BookPic/')
    publication_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk']