from django.db import models
from django.urls import reverse

from .author import Author
from .genre import Genre


class Book(models.Model):
    title = models.CharField(max_length=55, verbose_name="Название")
    genre = models.ManyToManyField(Genre, verbose_name="Жанр")
    pub_date = models.DateField(blank=True, null=True, verbose_name="Дата издания")
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Краткое описание")
    author = models.ManyToManyField(Author, verbose_name="Автор")

    class Meta:
        ordering = ["title"]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def get_absolute_url(self):
        return reverse('authors', args=(self.pk, ))

    def __str__(self):
        return self.title
