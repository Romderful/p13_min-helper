"""Animes serializers."""

from rest_framework import serializers
from .models import Anime, Category, Comment
from django.contrib.auth import get_user_model


class AnimeSerializer(serializers.ModelSerializer):
    """Animes serializer."""

    linked_animes = serializers.SerializerMethodField()

    def get_linked_animes(self, anime: Anime):
        """Return the animes that matches with the same categories."""
        substitutes = {}
        my_categories = anime.categories.all()
        animes = Anime.objects.filter(categories__in=my_categories)

        for anime in animes[:12]:
            selected_anime = [cat for cat in my_categories]
            linked_anime = [cat for cat in anime.categories.all()]
            similar_categories = len(set(selected_anime).intersection(linked_anime))
            substitutes[anime.id] = similar_categories

        substitutes = dict(sorted(substitutes.items(), key=lambda item: item[1])[::-1])
        sorted_substitutes = [anime for anime in substitutes]

        return sorted_substitutes

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


class CommentSerializer(serializers.ModelSerializer):
    """Comments serializer."""

    created_date = serializers.DateTimeField(
        format="%Y-%m-%d - %H:%M:%S", required=False, read_only=True
    )
    author = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(), slug_field="username"
    )

    class Meta:
        model = Comment
        fields = "__all__"
