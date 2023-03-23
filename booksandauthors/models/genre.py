from django.db import models
from django.urls import reverse


class Genre(models.Model):
    title = models.CharField(max_length=55, unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def get_absolute_url(self):
        return reverse("genre-detail", args=(self.pk,))

    def __str__(self):
        return self.title
