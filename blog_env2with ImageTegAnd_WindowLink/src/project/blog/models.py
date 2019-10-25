from django.db import models
from django.contrib.auth.models import User
# for image showing in admin panel
from django.utils.html import format_html

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='picture/')
    title = models.CharField(max_length=300)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    # showing image
    def image_tag(self):
        return format_html('<img src="/media/%s" width="100"/>'%self.image)
    #changing image field name
    image_tag.short_description = 'Image'

    class Meta:
        db_table ='Blog_Post'
        ordering = ["-id"]
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


