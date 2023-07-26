import random

from django.core.management.base import BaseCommand

from booksandauthors.models import Author, Book, Genre

from faker import Faker


class Command(BaseCommand):
    help = "Add some authors and books"

    def handle(self, *args, **options) -> None:
        fake = Faker(["ru_RU"])
        genres = ["Роман", "Детектив", "Ужасы", "Cтихи", "Пьеса"]
        if Author.objects.count() == 0:
            authors_objects_list = []
            genres_objects_list = [
                Genre.objects.create(title=title) for title in genres
            ]
            for _ in range(25):
                first_name = fake.first_name()
                second_name = fake.last_name()
                author_object = Author.objects.create(
                    first_name=first_name, second_name=second_name
                )
                authors_objects_list.append(author_object)

            for _ in range(25):
                book_title = fake.text(max_nb_chars=20)
                book_object = Book.objects.create(title=book_title)

                random_count = random.randint(1, 3)

                book_object.author.set(
                    random.sample(authors_objects_list, random_count)
                )
                book_object.genre.set(random.sample(genres_objects_list, random_count))

            print("Test base was filled")

        else:
            print("Test base is not empty")
