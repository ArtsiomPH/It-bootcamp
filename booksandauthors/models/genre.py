from django.db import models
from django.urls import reverse


class Genre(models.Model):
    title = models.CharField(max_length=55, unique=True, verbose_name="Название")

    class Meta:
        ordering = ["title"]
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def get_absolute_url(self) -> None:
        return reverse("genre-detail", args=(self.pk,))

    def __str__(self) -> models.CharField:
        return self.title
