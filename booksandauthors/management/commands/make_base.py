import random

from django.core.management.base import BaseCommand

from booksandauthors.models import Author, Book

AUTHORS = [
    {
        'first_name': 'Александр',
        'second_name': 'Пушкин'
    },
{
        'first_name': 'Лев',
        'second_name': 'Толстой'
    },
{
        'first_name': 'Сергей',
        'second_name': 'Есенин'
    },

]

BOOKS = [
    {
        'title': 'Евгений Онегин'
    },
{
        'title': 'Анна Каренина'
    },
{
        'title': 'Сборник стихов'
    },

]


class Command(BaseCommand):
    help = "Add some authors and books"

    def handle(self, *args, **options):
        authors_list = []
        for author in AUTHORS:
            author_object, _ = Author.objects.get_or_create(**author)
            authors_list.append(author_object)

        for book in BOOKS:
            book_object, _ = Book.objects.get_or_create(**book)
            book_object.author.set([random.choice(authors_list)])




