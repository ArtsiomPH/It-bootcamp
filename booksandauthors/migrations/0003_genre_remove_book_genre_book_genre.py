# Generated by Django 4.1.7 on 2023-03-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booksandauthors", "0002_book_genre"),
    ]

    operations = [
        migrations.CreateModel(
            name="Genre",
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
                ("title", models.CharField(max_length=55, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="book",
            name="genre",
        ),
        migrations.AddField(
            model_name="book",
            name="genre",
            field=models.ManyToManyField(
                to="booksandauthors.genre", verbose_name="Жанр"
            ),
        ),
    ]
