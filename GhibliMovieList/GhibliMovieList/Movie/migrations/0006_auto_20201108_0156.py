# Generated by Django 3.1.3 on 2020-11-07 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0005_movie_people'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='people',
            new_name='character',
        ),
    ]
