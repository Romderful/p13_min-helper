"""Animes serializers."""

from rest_framework import serializers
from .models import Anime, Category, Comment, Favourite
from django.contrib.auth import get_user_model


class AnimeSerializer(serializers.ModelSerializer):
    """Animes serializer."""

    linked_animes = serializers.SerializerMethodField()
    is_favourite = serializers.SerializerMethodField()

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

    def get_is_favourite(self, anime: Anime) -> bool:
        """Return true is the current anime is on favourite."""

        user = self.context["request"].user
        return Favourite.objects.filter(user=user, anime=anime).exists()

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

    anime = serializers.SerializerMethodField()

    def get_anime(self, instance):

        queryset = instance.anime
        serializer = AnimeSerializer(
            queryset, context={"request": self.context["request"]}
        )

        return serializer.data

    # def to_representation(self, instance):
    #     result = {}
    #     instance = instance.first()
    #     if not instance:
    #         return result
    #     result["user"] = instance.user.username
    #     result["anime"] = AnimeSerializer(
    #         instance=instance.anime, context={"request": self.context["request"]}
    #     ).data
    #     return result

    def create(self, validated_data):
        favourite = Favourite.objects.filter(
            user=validated_data["user"], anime=validated_data["anime"]
        )
        if favourite.exists():
            favourite.delete()

        else:
            Favourite.objects.create(
                user=validated_data["user"], anime=validated_data["anime"]
            )
        return favourite

    class Meta:
        model = Favourite
        fields = "__all__"
