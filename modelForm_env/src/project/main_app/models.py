from django.db import models

# Create your models here.
class ModelFormOne(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='picture/')

    def __str__(self):
        return self.title
class ModelFormTwo(models.Model):
    heading = models.CharField(max_length=300)
    image = models.ImageField(upload_to='picture/')

    def __str__(self):
        return self.heading