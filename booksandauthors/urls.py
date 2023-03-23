from django.urls import path

from .views import AuthorListView, AuthorDetailView, BookListView, BookDetailView, AuthorFormView


urlpatterns = [
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/', BookListView.as_view(), name='books-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('authors/', AuthorListView.as_view(), name='authors-list'),
    path('authors/add/', AuthorFormView.as_view(), name='author-create'),
]