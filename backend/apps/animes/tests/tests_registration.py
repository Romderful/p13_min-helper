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
        self.assertEqual(response.data["user"]["username"], "test")
