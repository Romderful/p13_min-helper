"""Animes models."""

from django.db import models
from django.contrib.auth import get_user_model


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

    categories = models.ManyToManyField(Category)
    update_date = models.DateTimeField(auto_now=True)
    english_name = models.CharField(max_length=175, blank=True, null=True)
    japanese_name = models.CharField(max_length=175, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.CharField(max_length=25, blank=True, null=True)
    end_date = models.CharField(max_length=25, blank=True, null=True)
    episodes_count = models.SmallIntegerField(blank=True, null=True)
    cover_image = models.URLField(blank=True, null=True)
    score = models.SmallIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        """Display the english name of the anime in the admin panel."""
        return self.english_name


class Favourite(models.Model):
    """Favourite's table."""

    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    anime = models.ForeignKey(Anime, on_delete=models.PROTECT)

    def __str__(self) -> str:
        """Display the email of the user in the admin panel."""
        return self.user.email
