# Generated by Django 5.2.1 on 2025-06-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_book_language_book_language_case_insensitive_unique'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='book',
            name='language_case_insensitive_unique',
        ),
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='language',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
