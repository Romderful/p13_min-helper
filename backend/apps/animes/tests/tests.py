from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):
    def test_registration(self):

        data = {
            "username": "test",
            "email": "test@gmail.com",
            "password1": "some_password",
            "password2": "some_password",
        }

        response = self.client.post("/api-v1/auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AnimeViewsetTestCase(APITestCase):

    list_url = reverse("animes-list")

    def setUp(self):

        user = get_user_model()

        user.objects.create_user(
            username="test",
            email="test@gmail.com",
            password="some_password",
        )

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
