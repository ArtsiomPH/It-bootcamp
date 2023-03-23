from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Author, Book, Genre


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


