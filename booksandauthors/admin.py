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

    @admin.display(description="Авторы")
    def get_authors(self, obj: Book) -> str:
        return ", ".join([str(author) for author in obj.author.all()])

    @admin.display(description="Жанры")
    def get_genres(self, obj: Book) -> str:
        return ", ".join([str(genre) for genre in obj.genre.all()])


@admin.register(Genre, site=admin.site)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_display_links = ("title",)
