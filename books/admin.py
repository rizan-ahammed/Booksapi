from django.contrib import admin
from books.models import Category, Book


class BookAdmin(admin.ModelAdmin):
    list_display=("id", "title")

    
admin.site.register(Book,BookAdmin)
admin.site.register(Category)
