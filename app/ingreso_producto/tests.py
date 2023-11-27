from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from .models import TipoIngreso, IngresoProducto

APP_URL_NAME = "ingreso_producto:"

class TipoIngresoTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email="test@test.com", password="test1234")
        self.tipo = TipoIngreso.objects.create(nombre="tipo")
        self.app_name = "ingreso_producto:"
        self.url_list = "tipoingreso-list"
        self.url_detail = "tipoingreso-detail"

    def test_list(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        data = {
            "nombre": "nobmre tipo"
        }
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_detail, kwargs={"pk": self.tipo.pk})
        data = {
            "nombre": "tipo cambiado"
        }
        response = self.client.patch(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tipo.refresh_from_db()
        self.assertEqual(self.tipo.nombre, data.get("nombre"))

    def test_delete(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_detail, kwargs={"pk": self.tipo.pk})
        response = self.client.delete(url,)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



class IngresoProductoTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email="test@test.com", password="test1234")
        self.instance_model = IngresoProducto.objects.create(fecha_ingreso=timezone.now().date())
        self.url_list = "ingresoproducto-list"
        self.url_detail = "ingresoproducto-detail"

    def test_list(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        data = {
            "fecha_ingreso": "2023-02-02",
            "ticket": "TiC",
        }
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_detail, kwargs={"pk": self.instance_model.pk})
        data = {
            "fecha_ingreso": "2023-02-03"
        }
        response = self.client.patch(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.instance_model.refresh_from_db()
        self.assertEqual(str(self.instance_model.fecha_ingreso), data.get("fecha_ingreso"))

    def test_delete(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_detail, kwargs={"pk": self.instance_model.pk})
        response = self.client.delete(url,)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


