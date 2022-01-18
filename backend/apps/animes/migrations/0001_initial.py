# Generated by Django 4.0.1 on 2022-01-17 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.CharField(max_length=75)),
                ('japanese_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('episodes_count', models.SmallIntegerField()),
                ('episode_duration', models.SmallIntegerField()),
                ('cover_image', models.URLField()),
                ('banner_image', models.URLField()),
                ('score', models.SmallIntegerField()),
                ('category', models.ManyToManyField(to='animes.Category')),
            ],
        ),
    ]