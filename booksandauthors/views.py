from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse

from .models import Author, Book, Genre


class AuthorListView(ListView):
    model = Author
    paginate_by = 20
    template_name = "authors_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = context["header"] = "Авторы"
        context["head_table"] = ["Фамилия", "Имя", "Отчество", "Дата Рождения"]
        return context


class AuthorCreateView(CreateView):
    model = Author
    fields = "__all__"
    template_name = "create.html"
    success_url = reverse_lazy("authors-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Добавить автора"
        return context


class AuthorUpdateView(UpdateView):
    model = Author
    fields = "__all__"
    template_name = "create.html"
    success_url = reverse_lazy("authors-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Изменение данных"
        return context


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy("authors-list")
    template_name = "confirm_delete.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Подтверждение удаления"
        context["url"] = reverse("authors-list")
        return context


class BookListView(ListView):
    queryset = Book.objects.prefetch_related("author").prefetch_related("genre").all()
    paginate_by = 20
    template_name = "books_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = context["header"] = "Книги"
        context["head_table"] = ["Название", "Жанр", "Год издания", "Авторы"]
        return context


class BookCreateView(CreateView):
    queryset = Book.objects.prefetch_related("author").prefetch_related("genre").all()
    fields = "__all__"
    template_name = "create.html"
    success_url = reverse_lazy("books-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Добавить книгу"
        return context


class BookUpdateView(UpdateView):
    queryset = Book.objects.prefetch_related("author").prefetch_related("genre").all()
    fields = "__all__"
    template_name = "create.html"
    success_url = reverse_lazy("books-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Изменение данных"
        return context


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("books-list")
    template_name = "confirm_delete.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Подтверждение удаления"
        context["url"] = reverse("books-list")
        return context


class GenreListView(ListView):
    model = Genre
    paginate_by = 20
    template_name = "genres_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = context["header"] = "Жанры"
        context["head_table"] = ["Название"]
        return context


class GenreCreateView(CreateView):
    model = Genre
    fields = "__all__"
    template_name = "create.html"
    success_url = reverse_lazy("genres-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Добавить жанр"
        return context


class GenreUpdateView(UpdateView):
    model = Genre
    fields = "__all__"
    template_name = "create.html"
    success_url = reverse_lazy("genres-list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Изменение данных"
        return context


class GenreDeleteView(DeleteView):
    model = Genre
    success_url = reverse_lazy("genres-list")
    template_name = "confirm_delete.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["title"] = "Подтверждение удаления"
        context["url"] = reverse("genres-list")
        return context
