"""Animes urls."""

from rest_framework.routers import SimpleRouter
from .views import AnimeViewSet, CategoryViewSet, CommentViewSet


router = SimpleRouter()
router.register("animes", AnimeViewSet, basename="animes")
router.register("animes-categories", CategoryViewSet, basename="categories")
router.register("animes-comments", CommentViewSet, basename="comments")

urlpatterns = router.urls
