from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db import transaction

from drf_spectacular.utils import extend_schema, OpenApiExample

from operacional.api.serializer.ingreso_producto_tanque_serializer import IngresoProductoTanqueSerializer

from operacional.models import IngresoProductoTanque, HistorialIngresoProductoTanque, Tanque

from decimal import Decimal


class IngresoProductoTanqueViewSet(ModelViewSet):
    queryset = IngresoProductoTanque.objects.all()
    serializer_class = IngresoProductoTanqueSerializer

    filterset_fields = {
        "tanque": ["exact"],
        "ingreso_producto": ["exact"],
        "fecha": ["gte", "gt", "lt", "lte", "exact"],
    }

    def get_serializer_class(self):
        return super().get_serializer_class()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        instance = serializer.save()
        HistorialIngresoProductoTanque.objects.create(
            ingreso_producto = instance.ingreso_producto,
            tanque_origen =None,
            tanque_destino =instance.tanque,
            ingreso_producto_tanque=instance,
            cantidad =instance.cantidad,
            fecha = instance.fecha,
        )

    @extend_schema(
        responses={200: {"ingreso_producto_tanque": 1}},
        methods=["patch"],
        examples=[
         OpenApiExample(
            'Valid example 1',
            summary='enviar cantidad a otro tanque',
            description=' se debe enviar el id del ingreso producto tanque ',
            value={
                'cantidad_destino': "10",
                'tanque_destino': "1"
            },
            request_only=True, # signal that example only applies to requests
        ),
    ]
    )
    @transaction.atomic
    @action(detail=True, methods=['patch'])
    def enviar_a_otro_tanque(self, request, *args, **kwargs):
        instance = self.get_object()

        #data = {"cantidad_destino", "tanque_destino", }
        data = {
            "cantidad": instance.cantidad - Decimal(request.data.get("cantidad_destino")).quantize(Decimal('.0001'))
        }
        tanque_destino = Tanque.objects.get(pk=request.data.get('tanque_destino'))
        if tanque_destino.capacidad_disponible - Decimal(request.data.get("cantidad_destino")).quantize(Decimal('.0001')) < 0:
            return Response({"error": "Cantidad no adecuada, el tanque no tiene ese tamaño disponible"}, status=400)
        
        if instance.cantidad - Decimal(request.data.get("cantidad_destino")).quantize(Decimal('.0001')) < 0: 
            return Response({"error": "Cantidad no adecuada, excede a la transferencia original"}, status=400)
        instance.cantidad = data["cantidad"]
        instance.save()
        ingreso_producto_tanque = IngresoProductoTanque.objects.create(
            ingreso_producto = instance.ingreso_producto,
            tanque_id = request.data.get('tanque_destino'),
            cantidad = request.data.get("cantidad_destino"),
            fecha =instance.fecha
        )
        HistorialIngresoProductoTanque.objects.create(
            ingreso_producto = instance.ingreso_producto,
            tanque_origen =instance.tanque,
            tanque_destino_id =request.data.get('tanque_destino'),
            ingreso_producto_tanque=instance,
            cantidad =instance.cantidad,
            fecha = instance.fecha,
        )
        tanque_destino.capacidad_disponible -= Decimal(request.data.get("cantidad_destino")).quantize(Decimal('.0001'))
        tanque_destino.save()

        return Response(data={
            "ingreso_producto_tanque": ingreso_producto_tanque.pk,

        })
        
