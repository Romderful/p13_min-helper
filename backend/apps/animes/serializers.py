"""Animes serializers."""

from rest_framework import serializers
from .models import Anime, Category


class AnimeSerializer(serializers.ModelSerializer):
    """Animes serializer."""

    linked_animes = serializers.SerializerMethodField()

    def get_linked_animes(self, anime: Anime):
        """Return the animes that matches with the same genres."""
        my_categories = anime.categories.all()
        animes = Anime.objects.filter(categories__in=my_categories)[:9]
        return [anime.english_name for anime in animes]

    categories = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = Anime
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """Categories serializer."""

    class Meta:
        model = Category
        fields = "__all__"
