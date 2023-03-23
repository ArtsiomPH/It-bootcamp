from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .models import Author, Book, Genre
from .forms import AuthorForm


class AuthorListView(ListView):
    model = Author
    paginate_by = 20
    template_name = 'authors_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Авторы'
        return context


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


class AuthorFormView(CreateView):
    model = Author
    fields = '__all__'
    template_name = 'author_create.html'
    success_url = reverse_lazy('authors-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Добавить автора'
        return context


class BookListView(ListView):
    model = Book
    paginate_by = 20
    template_name = 'books_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Книги'
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
