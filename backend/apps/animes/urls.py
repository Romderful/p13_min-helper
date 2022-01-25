"""Animes urls."""

from rest_framework.routers import SimpleRouter
from .views import AnimeViewSet, CategoryViewSet


router = SimpleRouter()
router.register("animes", AnimeViewSet, basename="animes")
router.register("animes-categories", CategoryViewSet, basename="categories")

urlpatterns = router.urls
