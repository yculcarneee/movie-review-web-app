# Generated by Django 3.1.5 on 2021-01-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatchedMoviesDatabase',
            fields=[
                ('movieId', models.IntegerField(primary_key=True, serialize=False)),
                ('movieName', models.TextField()),
            ],
        ),
    ]
