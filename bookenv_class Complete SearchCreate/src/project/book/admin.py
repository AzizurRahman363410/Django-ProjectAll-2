from django.contrib import admin
from .models import Book

# Register your models here.

class BookPostAdmin(admin.ModelAdmin):
    search_fields = ['title','authors','publisher']
    list_filter = ['title','authors','publisher']
    list_display = ['title','authors','publication_date']
    list_display_links = ['title','publication_date']
    # remember list_display_link != list_editable bcz if it has link how field will be edit.
    list_editable = [ 'authors',]
    list_per_page = 5




admin.site.register(Book,BookPostAdmin)
