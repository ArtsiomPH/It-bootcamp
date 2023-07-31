from django.urls import path

from .views import (
    AuthorListView,
    AuthorDetailView,
    BookListView,
    BookDetailView,
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
    path("book/add/", BookCreateView.as_view(), name="book-create"),
    path("book/update/<int:pk>", BookUpdateView.as_view(), name="book-update"),
    path("book/delete/<int:pk>", BookDeleteView.as_view(), name="book-delete"),
    path("book/<int:pk>", BookDetailView.as_view(), name="book-detail"),
    path("authors/", AuthorListView.as_view(), name="authors-list"),
    path("author/<int:pk>", AuthorDetailView.as_view(), name="author-detail"),
    path("author/add/", AuthorCreateView.as_view(), name="author-create"),
    path("author/update/<int:pk>", AuthorUpdateView.as_view(), name="author-update"),
    path("author/delete/<int:pk>", AuthorDeleteView.as_view(), name="author-delete"),
    path("genres/", GenreListView.as_view(), name="genres-list"),
    path("genre/add/", GenreCreateView.as_view(), name="genre-create"),
    path("genre/update/<int:pk>", GenreUpdateView.as_view(), name="genre-update"),
    path("genre/delete/<int:pk>", GenreDeleteView.as_view(), name="genre-delete"),
]
