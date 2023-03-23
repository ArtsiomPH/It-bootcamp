from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=55, unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.title


