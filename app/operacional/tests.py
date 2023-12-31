from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from .models import TipoIngreso, IngresoProducto, Tanque, IngresoProductoTanque, HistorialIngresoProductoTanque, CalidadTanque

import decimal

APP_URL_NAME = "operacional:"

class TipoIngresoTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email="test@test.com", password="test1234")
        self.tipo = TipoIngreso.objects.create(nombre="tipo")
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
            "peso_bruto": None,
            "peso_tara": None,
        }
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("peso_neto"), '0.0000')

    def test_create_with_peso_neto(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        data = {
            "fecha_ingreso": "2023-02-02",
            "ticket": "TiC",
            "peso_bruto": 12,
            "peso_tara": 15.23,
        }
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("peso_neto"), '27.2300')

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


class TanqueTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email="test@test.com", password="test1234")
        self.instance_model = Tanque.objects.create(
            nombre="T1",
            capacidad= 100,
            capacidad_disponible=100,
        )
        self.url_list = "tanque-list"
        self.url_detail = "tanque-detail"

    def test_list_tanque(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_tanque_without_capacidad(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        data = {
            "nombre": "T2",
            "capacidad": None,
        }
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("capacidad_disponible"), '0.0000')

    def test_create_tanque_with_capacidad(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        data = {
            "nombre": "T2",
            "capacidad": "100",
        }
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("capacidad_disponible"), '100.0000')

    def test_update_tanque(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_detail, kwargs={"pk": self.instance_model.pk})
        data = {
            "capacidad": "100.0000",
        }
        response = self.client.patch(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.instance_model.refresh_from_db()
        self.assertEqual(self.instance_model.capacidad_disponible, decimal.Decimal("100.0000").quantize(decimal.Decimal('.0001')))

        IngresoProductoTanque.objects.create(
            ingreso_producto =None,
            tanque = self.instance_model,
            cantidad = 50,
            fecha = timezone.now().date(),
        )
        response = self.client.patch(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.instance_model.refresh_from_db()
        self.assertEqual(self.instance_model.capacidad_disponible, decimal.Decimal("50.0000").quantize(decimal.Decimal('.0001')))



class IngresoProductoTanqueTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email="test@test.com", password="test1234")
        self.instance_tanque = Tanque.objects.create(
            nombre="T1",
            capacidad= 100,
            capacidad_disponible=100,
        )
        self.instance_ingreso_producto = IngresoProducto.objects.create(
            fecha_ingreso=timezone.now().date(),
            peso_bruto = 200,
            peso_tara=100,
            peso_neto=100,
            peso_neto_disponible=100,
        )
        self.instance_model = IngresoProductoTanque.objects.create(
            ingreso_producto =self.instance_ingreso_producto,
            tanque = self.instance_tanque,
            cantidad = 50,
            fecha = timezone.now().date(),
        )
        self.url_base = "ingresoproductotanque"
        self.url_list = self.url_base +"-list"
        self.url_detail = self.url_base+"-detail"

    def test_list_ingreso_producto_tanque(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_with_new_ingreso(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        data = {
            "ingreso_producto": self.instance_ingreso_producto.pk,
            "tanque": self.instance_tanque.pk,
            "cantidad": 50,
            "fecha": "2023-08-08",
        }
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.instance_tanque.refresh_from_db()
        self.assertEqual(self.instance_tanque.capacidad_disponible, decimal.Decimal("50.0000").quantize(decimal.Decimal('.0001')))

        self.instance_ingreso_producto.refresh_from_db()
        self.assertEqual(self.instance_ingreso_producto.peso_neto_disponible, decimal.Decimal("50.0000").quantize(decimal.Decimal('.0001')))

    def test_create_with_new_ingreso_excess(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        self.instance_tanque.capacidad_disponible = 100
        self.instance_tanque.save()
        nuevo_ingreso = IngresoProducto.objects.create(
            fecha_ingreso=timezone.now().date(),
            peso_bruto = 200,
            peso_tara=100,
            peso_neto=100,
            peso_neto_disponible=100,
        )
        data = {
            "ingreso_producto": nuevo_ingreso.pk,
            "tanque": self.instance_tanque.pk,
            "cantidad": 101,
            "fecha": "2023-08-08",
        }
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.instance_tanque.refresh_from_db()
        self.assertEqual(self.instance_tanque.capacidad_disponible, 100)

    def test_enviar_a_otro_tanque(self):
        #enviar_a_otro_tanque
        self.client.force_authenticate(user=self.user)
        tanque_2 = Tanque.objects.create(
            nombre="T3",
            capacidad= 100,
            capacidad_disponible=100,
        )
        url = reverse(APP_URL_NAME+self.url_base+'-enviar-a-otro-tanque', kwargs={"pk": self.instance_model.pk})
        data = {
            "cantidad_destino": "10", 
            "tanque_destino": tanque_2.pk,
        }
        response = self.client.patch(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        tanque_2.refresh_from_db()
        self.assertEqual(tanque_2.capacidad_disponible, decimal.Decimal("90.0000").quantize(decimal.Decimal('.0001')))

        self.instance_model.refresh_from_db()
        self.assertEqual(self.instance_model.cantidad, decimal.Decimal("40.0000").quantize(decimal.Decimal('.0001')))

        self.assertTrue(HistorialIngresoProductoTanque.objects.filter(tanque_destino=tanque_2).exists)

    def test_enviar_a_otro_tanque_failed_ingreso(self):
        self.client.force_authenticate(user=self.user)
        tanque_3 = Tanque.objects.create(
            nombre="T3",
            capacidad= 100,
            capacidad_disponible=100,
        )
        url = reverse(APP_URL_NAME+self.url_base+'-enviar-a-otro-tanque', kwargs={"pk": self.instance_model.pk})
        data = {
            "cantidad_destino": float(self.instance_model.cantidad) +1, 
            "tanque_destino": tanque_3.pk,
        }
        response = self.client.patch(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_enviar_a_otro_tanque_failed_tanque(self):
        self.client.force_authenticate(user=self.user)
        tanque_3 = Tanque.objects.create(
            nombre="T3",
            capacidad= 50,
            capacidad_disponible=50,
        )
        url = reverse(APP_URL_NAME+self.url_base+'-enviar-a-otro-tanque', kwargs={"pk": self.instance_model.pk})
        if self.instance_model.cantidad < 51:
            self.instance_model.cantidad = 51
            self.instance_model.save()
        data = {
            "cantidad_destino": "51", 
            "tanque_destino": tanque_3.pk,
        }
        response = self.client.patch(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class HistorialIngresoProductoTanqueTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email="test@test.com", password="test1234")
        self.instance_tanque = Tanque.objects.create(
            nombre="T1",
            capacidad= 100,
            capacidad_disponible=100,
        )
        self.instance_ingreso_producto = IngresoProducto.objects.create(
            fecha_ingreso=timezone.now().date(),
            peso_bruto = 200,
            peso_tara=100,
            peso_neto=100,
            peso_neto_disponible=100,
        )
        
        self.instance_model = HistorialIngresoProductoTanque.objects.create(
            ingreso_producto = self.instance_ingreso_producto,
            tanque_origen = None,
            tanque_destino = self.instance_tanque,
            ingreso_producto_tanque =None,
            cantidad = 100,
            fecha = timezone.now().date()
        )
        self.url_list = "historialingresoproductotanque-list"

    def test_list_historial(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_historial_with_params(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        response = self.client.get(url, data={"ingreso_producto": self.instance_ingreso_producto.pk})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_historial_with_params_without_res(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        ingreso_test = IngresoProducto.objects.create(
            fecha_ingreso=timezone.now().date(),
            peso_bruto = 200,
            peso_tara=100,
            peso_neto=100,
            peso_neto_disponible=100,
        )
        response = self.client.get(url, data={"ingreso_producto": ingreso_test.pk})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class CalidadTanqueTest(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email="test@test.com", password="test1234")
        self.tanque = Tanque.objects.create(
            nombre="T1",
        )
        self.calidad_tanque_instance = CalidadTanque.objects.create(tanque=self.tanque)
        self.url_list = "calidadtanque-list"
        self.url_detail = "calidadtanque-detail"

    def test_list_calidad_tanque(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_calidad_tanque_query_params_with_response(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        response = self.client.get(url, data={"tanque": self.tanque.pk})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_calidad_tanque_query_params_empty_response(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        tanque = Tanque.objects.create(nombre="T3")
        response = self.client.get(url, data={"tanque": tanque.pk})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_calidad_tanque(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_list)
        tanque = Tanque.objects.create(nombre="T2")
        data = {
            "tanque": tanque.pk,
        }
        response = self.client.post(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_detail, kwargs={"pk": self.calidad_tanque_instance.pk})
        data = {
            "anisidina": "100.000"
        }
        response = self.client.patch(url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.calidad_tanque_instance.refresh_from_db()
        self.assertEqual(self.calidad_tanque_instance.anisidina, decimal.Decimal(data.get("anisidina")).quantize(decimal.Decimal('.0001')))

    def test_delete(self):
        self.client.force_authenticate(user=self.user)
        url = reverse(APP_URL_NAME+self.url_detail, kwargs={"pk": self.calidad_tanque_instance.pk})
        response = self.client.delete(url,)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(CalidadTanque.objects.filter(pk=self.calidad_tanque_instance.pk).exists())



