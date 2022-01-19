"""Animes views."""

from rest_framework import viewsets
from .models import Anime
from .serializers import AnimeSerializer


class AnimeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Anime.objects.all().order_by("id")
    serializer_class = AnimeSerializer
