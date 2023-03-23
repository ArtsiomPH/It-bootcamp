# Generated by Django 4.1.7 on 2023-03-23 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=55, verbose_name="Имя")),
                (
                    "second_name",
                    models.CharField(max_length=55, verbose_name="Фамилия"),
                ),
                (
                    "third_name",
                    models.CharField(
                        blank=True, max_length=55, null=True, verbose_name="Отчество"
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата рождения"
                    ),
                ),
                (
                    "biography",
                    models.TextField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="Краткая биография",
                    ),
                ),
            ],
            options={
                "ordering": ["second_name", "first_name"],
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=55, verbose_name="Название")),
                (
                    "pub_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата издания"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="Краткое описание",
                    ),
                ),
                (
                    "author",
                    models.ManyToManyField(
                        to="booksandauthors.author", verbose_name="Автор"
                    ),
                ),
            ],
            options={
                "ordering": ["title"],
            },
        ),
    ]
