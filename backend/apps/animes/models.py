"""Animes models."""

from django.db import models


class Category(models.Model):
    """Category's table."""

    class Meta:
        """Change the plural of category from 'categorys' to 'categories'."""

        verbose_name_plural = "categories"

    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        """Display the name of the category in the admin panel."""
        return self.name


class Anime(models.Model):
    """Anime's table."""

    category = models.ManyToManyField(Category)
    update_date = models.DateTimeField(auto_now=True)
    english_name = models.CharField(max_length=75)
    japanese_name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    episodes_count = models.SmallIntegerField()
    episode_duration = models.SmallIntegerField()
    cover_image = models.URLField(max_length=200)
    banner_image = models.URLField(max_length=200)
    score = models.SmallIntegerField()

    def __str__(self) -> str:
        """Display the english name of the anime in the admin panel."""
        return self.english_name
