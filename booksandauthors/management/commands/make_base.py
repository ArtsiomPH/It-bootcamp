import random

from django.core.management.base import BaseCommand

from booksandauthors.models import Author, Book

from faker import Faker


class Command(BaseCommand):
    help = "Add some authors and books"

    def handle(self, *args, **options) -> None:
        fake = Faker(["ru_RU"])
        if Author.objects.count() == 0:
            authors_list = []
            for _ in range(25):
                first_name = fake.first_name()
                second_name = fake.last_name()
                author_object = Author.objects.create(
                    first_name=first_name, second_name=second_name
                )
                authors_list.append(author_object)

            for _ in range(25):
                book_title = fake.text(max_nb_chars=20)
                book_object = Book.objects.create(title=book_title)

                authors_count = random.randint(1, 3)
                book_object.author.set(random.sample(authors_list, authors_count))

            print("Test base was filled")

        else:
            print("Test base is not empty")
