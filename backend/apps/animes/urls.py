"""Animes urls."""

from rest_framework.routers import SimpleRouter
from .views import AnimeViewSet, CategoryViewSet, CommentViewSet, FavouriteViewSet


router = SimpleRouter()
router.register("animes", AnimeViewSet, basename="animes")
router.register("animes-categories", CategoryViewSet, basename="categories")
router.register("animes-comments", CommentViewSet, basename="comments")
router.register("animes-favourites", FavouriteViewSet, basename="favourites")

urlpatterns = router.urls
