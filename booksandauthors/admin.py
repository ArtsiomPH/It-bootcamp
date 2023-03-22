from django.contrib import admin
from .models import Author, Book


@admin.register(Author, site=admin.site)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book, site=admin.site)
class BookAdmin(admin.ModelAdmin):
    pass
