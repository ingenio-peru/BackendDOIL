from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from django.contrib.auth import get_user_model


class AuthTest(APITestCase):
    user_email = "test@test.com"
    user_pass = "password"

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email=self.user_email, password=self.user_pass)

    def test_login(self):
        url = reverse("core:auth-login")
        data = {
            "email": self.user_email,
            "password": self.user_pass,
        }
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_login_with_user(self):
        url = reverse("core:auth-login")
        data = {
            "email": "email@sinusuario.com",
            "password": "password",
        }
        response = self.client.post(url, data=data, format="json")

        self.assertNotEqual(response.status_code, status.HTTP_200_OK)


class UserTest(APITestCase):
    user_email = "test@test.com"
    user_pass = "password"

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email=self.user_email, password=self.user_pass)

    def test_user_create(self):
        url = reverse("core:create-user")
        data = {
            "email": "email@sinusuario.com",
            "password": "password",
            "name": "nombre",
        }
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(get_user_model().objects.count(), 2)


    def test_me(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("core:me",)
        data = {
            "name": "nombre",
        }
        response = self.client.patch(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user.refresh_from_db()

        self.assertEqual(self.user.name, data.get("name"))
