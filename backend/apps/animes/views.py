"""Animes views."""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from .models import Anime, Category, Comment, Favourite
from .serializers import (
    AnimeSerializer,
    CategorySerializer,
    CommentSerializer,
    FavouriteSerializer,
)
from .pagination import LargeResultsSetPagination


class AnimeViewSet(viewsets.ReadOnlyModelViewSet):
    """Animes model viewset."""

    serializer_class = AnimeSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["english_name", "japanese_name"]
    ordering_fields = ["start_date", "end_date", "score"]

    def get_queryset(self):
        queryset = Anime.objects.all().order_by("-start_date")
        category = self.request.query_params.get("categories")
        if category is not None:
            queryset = queryset.filter(categories__name=category.title())
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Categories model viewset."""

    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    pagination_class = LargeResultsSetPagination


class CommentViewSet(viewsets.ModelViewSet):
    """Comments model viewset."""

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["anime"]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FavouriteViewSet(viewsets.ModelViewSet):
    """Categories model viewset."""

    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    pagination_class = LargeResultsSetPagination
