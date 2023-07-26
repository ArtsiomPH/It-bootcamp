import random

from django.core.management.base import BaseCommand

from booksandauthors.models import Author, Book


class Command(BaseCommand):
    help = "Add some authors and books"

    def handle(self, *args, **options) -> None:
        if Author.objects.count() == 0:
            authors_list = []
            for counter in range(20):
                first_name = f"Имя {counter}"
                second_name = f"Фамилия {counter}"
                author_object, _ = Author.objects.get_or_create(
                    first_name=first_name, second_name=second_name
                )
                authors_list.append(author_object)

            for counter in range(len(authors_list)):
                title = f"Название {counter}"
                book_object, _ = Book.objects.get_or_create(title=title)
                book_object.author.set([random.choice(authors_list)])

            print("Test base was filled")

        else:
            print("Test base is not already empty")
