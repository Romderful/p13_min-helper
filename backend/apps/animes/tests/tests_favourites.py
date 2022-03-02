from apps.animes.models import Anime, Favourite
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class FavouriteViewsetTestCase(APITestCase):

    list_url = reverse("favourites-list")

    def setUp(self):

        user = get_user_model()

        user = user.objects.create_user(
            username="test_name",
            email="test@gmail.com",
            password="some_password",
        )

        auth_token = self.client.post(
            "/api-v1/auth/login/",
            {"email": "test@gmail.com", "password": "some_password"},
        ).data.get("access_token")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")

        anime = Anime.objects.create(
            id=1,
            english_name="test_name",
            description="test_description",
            cover_image="https://test_image.com",
        )

        Favourite.objects.create(user=user, anime=anime)

    def test_favourite_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_favourite_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_favourite_detail_retrieve(self):
        response = self.client.get(reverse("favourites-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], "test_name")
        self.assertEqual(response.data["anime"], 1)
