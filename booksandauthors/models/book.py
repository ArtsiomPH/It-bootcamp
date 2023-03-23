from django.db import models

from ..models import Author


class Book(models.Model):
    title = models.CharField(max_length=55, verbose_name="Название")
    genre = models.CharField(max_length=25, blank=True, null=True, verbose_name="Жанр")
    pub_date = models.DateField(blank=True, null=True, verbose_name="Дата издания")
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Краткое описание")
    author = models.ManyToManyField(Author, verbose_name="Автор")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title