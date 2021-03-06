from apps.animes.models import Anime
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AnimeViewsetTestCase(APITestCase):

    list_url = reverse("animes-list")

    def setUp(self):

        user = get_user_model()

        user.objects.create_user(
            username="test",
            email="test@gmail.com",
            password="some_password",
        )

        anime = Anime.objects.create(
            english_name="test_name",
            description="test_description",
            cover_image="https://test_image.com",
        )

        anime.categories.create(name="test_category")

        auth_token = self.client.post(
            "/api-v1/auth/login/",
            {"email": "test@gmail.com", "password": "some_password"},
        ).data.get("access_token")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")

    def test_anime_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anime_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_anime_detail_retrieve(self):
        response = self.client.get(reverse("animes-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["english_name"], "test_name")
        self.assertEqual(response.data["description"], "test_description")
        self.assertEqual(response.data["cover_image"], "https://test_image.com")
        self.assertEqual(response.data["categories"][0], "test_category")
