"""Animes views."""

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from .models import Anime, Category
from .serializers import AnimeSerializer, CategorySerializer
from .pagination import LargeResultsSetPagination


class AnimeViewSet(viewsets.ReadOnlyModelViewSet):
    """Animes model viewset."""

    serializer_class = AnimeSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["english_name", "japanese_name"]
    ordering_fields = ["start_date", "end_date", "score"]

    def get_queryset(self):
        queryset = Anime.objects.all().order_by("-score")
        category = self.request.query_params.get("categories")
        if category is not None:
            queryset = queryset.filter(categories__name=category.title())
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Categories model viewset."""

    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    pagination_class = LargeResultsSetPagination
