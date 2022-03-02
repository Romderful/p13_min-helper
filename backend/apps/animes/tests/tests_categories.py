from apps.animes.models import Category
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CategoryViewsetTestCase(APITestCase):

    list_url = reverse("categories-list")

    def setUp(self):

        user = get_user_model()

        user.objects.create_user(
            username="test",
            email="test@gmail.com",
            password="some_password",
        )

        Category.objects.create(id=1, name="test_name")

        auth_token = self.client.post(
            "/api-v1/auth/login/",
            {"email": "test@gmail.com", "password": "some_password"},
        ).data.get("access_token")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")

    def test_category_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_category_detail_retrieve(self):
        response = self.client.get(reverse("categories-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "test_name")
