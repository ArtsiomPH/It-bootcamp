from django.urls import path

from .views import (
    AuthorListView,
    BookListView,
    AuthorCreateView,
    BookCreateView,
    AuthorUpdateView,
    AuthorDeleteView,
    BookUpdateView,
    BookDeleteView,
    GenreListView,
    GenreCreateView,
    GenreUpdateView,
    GenreDeleteView,
)

urlpatterns = [
    path("books/", BookListView.as_view(), name="books-list"),
    path("books/add/", BookCreateView.as_view(), name="book-create"),
    path("books/update/<int:pk>", BookUpdateView.as_view(), name="book-update"),
    path("books/delete/<int:pk>", BookDeleteView.as_view(), name="book-delete"),
    path("authors/", AuthorListView.as_view(), name="authors-list"),
    path("authors/add/", AuthorCreateView.as_view(), name="author-create"),
    path("authors/update/<int:pk>", AuthorUpdateView.as_view(), name="author-update"),
    path("authors/delete/<int:pk>", AuthorDeleteView.as_view(), name="author-delete"),
    path("genres/", GenreListView.as_view(), name="genres-list"),
    path("genres/add/", GenreCreateView.as_view(), name="genre-create"),
    path("genres/update/<int:pk>", GenreUpdateView.as_view(), name="genre-update"),
    path("genres/delete/<int:pk>", GenreDeleteView.as_view(), name="genre-delete"),
]
