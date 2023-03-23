from django.contrib import admin
from .models import Author, Book, Genre


@admin.register(Author, site=admin.site)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("second_name", "first_name", "third_name", "date_of_birth")
    list_display_links = ("second_name",)


@admin.register(Book, site=admin.site)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "get_genres", "pub_date", "get_authors")
    list_display_links = ("title",)

    def get_authors(self, obj):
        return ", ".join([str(author) for author in obj.author.all()])

    def get_genres(self, obj):
        return ", ".join([str(genre) for genre in obj.genre.all()])

    get_authors.short_description = "Авторы"
    get_genres.short_description = "Жанры"


@admin.register(Genre, site=admin.site)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_display_links = ("title",)
