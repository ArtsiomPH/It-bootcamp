from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Author, Book, Genre


class AuthorListView(ListView):
    model = Author
    paginate_by = 20
    template_name = "authors_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Авторы"
        return context


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"


class AuthorCreateView(CreateView):
    model = Author
    fields = "__all__"
    template_name = "author_create.html"
    success_url = reverse_lazy("authors-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Добавить автора"
        return context


class AuthorUpdateView(UpdateView):
    model = Author
    fields = "__all__"
    template_name = "author_create.html"
    success_url = reverse_lazy("authors-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Изменение данных"
        return context


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy("authors-list")
    template_name = "author_confirm_delete.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Подтверждение удаления"
        return context


class BookListView(ListView):
    model = Book
    paginate_by = 20
    template_name = "books_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Книги"
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"


class BookCreateView(CreateView):
    model = Book
    fields = "__all__"
    template_name = "book_create.html"
    success_url = reverse_lazy("books-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Добавить книгу"
        return context


class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = "book_create.html"
    success_url = reverse_lazy("books-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Изменение данных"
        return context


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("books-list")
    template_name = "book_confirm_delete.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Подтверждение удаления"
        return context
