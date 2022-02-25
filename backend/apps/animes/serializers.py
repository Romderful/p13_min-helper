"""Animes serializers."""

from rest_framework import serializers
from .models import Anime, Category, Comment, Favourite
from django.contrib.auth import get_user_model


class AnimeSerializer(serializers.ModelSerializer):
    """Animes serializer."""

    linked_animes = serializers.SerializerMethodField()
    is_favourite = serializers.SerializerMethodField()
    favourite_id = serializers.SerializerMethodField()
    added_to_favourites = serializers.SerializerMethodField()

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

        substitutes = [
            category
            for category, _ in sorted(
                substitutes.items(), key=lambda item: item[1], reverse=True
            )
        ]

        return substitutes

    def get_added_to_favourites(self, anime: Anime):
        """Return the number of times this anime has been added to the favourites."""
        return Favourite.objects.filter(anime=anime).count()

    def get_is_favourite(self, anime: Anime) -> bool:
        """Return a boolean depending if the favourite exists."""

        user = self.context["request"].user
        return Favourite.objects.filter(user=user, anime=anime).exists()

    def get_favourite_id(self, anime: Anime) -> int:
        """Return the id of the selected favourite."""

        user = self.context["request"].user
        return (
            Favourite.objects.filter(user=user, anime=anime)
            .values_list("id", flat=True)
            .first()
        )

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


class FavouriteSerializer(serializers.ModelSerializer):
    """Favourites serializer."""

    user = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(), slug_field="username"
    )
    anime_details = serializers.SerializerMethodField()

    def get_anime_details(self, instance):
        queryset = instance.anime
        serializer = AnimeSerializer(queryset, context=self.context)
        return serializer.data

    class Meta:
        model = Favourite
        fields = "__all__"
