# Generated by Django 4.1.7 on 2023-03-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksandauthors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Жанр'),
        ),
    ]
