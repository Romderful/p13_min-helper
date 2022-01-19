"""Animes urls."""

from rest_framework.routers import SimpleRouter
from .views import AnimeViewSet


router = SimpleRouter()
router.register("", AnimeViewSet, basename="animes")

urlpatterns = router.urls
