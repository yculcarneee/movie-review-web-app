# Generated by Django 3.1.5 on 2021-01-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieRatingDatabase',
            fields=[
                ('movieId', models.IntegerField(primary_key=True, serialize=False)),
                ('movieName', models.TextField()),
                ('movieRating', models.IntegerField()),
            ],
        ),
    ]
