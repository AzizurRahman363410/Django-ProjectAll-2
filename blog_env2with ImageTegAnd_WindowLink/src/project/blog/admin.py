from django.contrib import admin
from blog.models import Blog
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
# Register your models here.


# class BlogModelAdmin(admin.ModelAdmin):

class BlogModelAdmin(ImportExportModelAdmin):
    # def image_tag(self, obj):
    #     return format_html('<img src="media/picture/" />'.format(obj.image.url))
    #
    # image_tag.short_description = 'Image'


    list_display = ['id','title','description','image_tag','pub_date']
    list_display_links = ['title','image_tag',]
    list_editable = ['description',]
    search_fields = ['title','description',]
    list_per_page = 10


admin.site.register(Blog,BlogModelAdmin)