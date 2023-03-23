from django.urls import path

from .views import AuthorListView, AuthorDetailView

urlpatterns = [
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('authors/', AuthorListView.as_view(), name='authors-list'),
]