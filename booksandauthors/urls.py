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
)

urlpatterns = [
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/", BookListView.as_view(), name="books-list"),
    path("books/add/", BookCreateView.as_view(), name="book-create"),
    path("books/update/<int:pk>", BookUpdateView.as_view(), name="book-update"),
    path("books/delete/<int:pk>", BookDeleteView.as_view(), name="book-delete"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("authors/", AuthorListView.as_view(), name="authors-list"),
    path("authors/add/", AuthorCreateView.as_view(), name="author-create"),
    path("authors/update/<int:pk>", AuthorUpdateView.as_view(), name="author-update"),
    path("authors/delete/<int:pk>", AuthorDeleteView.as_view(), name="author-delete"),
]
