from django.db import models
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=55, verbose_name="Имя")
    second_name = models.CharField(max_length=55, verbose_name="Фамилия")
    third_name = models.CharField(
        max_length=55, verbose_name="Отчество", blank=True, null=True
    )
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name="Дата рождения"
    )
    biography = models.TextField(
        max_length=1000, verbose_name="Краткая биография", blank=True, null=True
    )

    class Meta:
        ordering = ["second_name", "first_name"]
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def get_absolute_url(self):
        return reverse("author-detail", args=(self.pk,))

    def __str__(self):
        if self.third_name:
            return (
                f"{self.second_name} "
                + f"{self.first_name}"[0]
                + "."
                + f"{self.third_name}"[0]
                + "."
            )
        return f"{self.second_name} " + f"{self.first_name}"[0] + "."
