from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db import transaction


from operacional.api.serializer.historial_ingreso_producto_tanque_serializer import HistorialIngresoProductoTanqueSerializer

from operacional.models import HistorialIngresoProductoTanque



class HistorialIngresoProductoTanqueViewSet(ModelViewSet):
    queryset = HistorialIngresoProductoTanque.objects.all().select_related('ingreso_producto')
    serializer_class = HistorialIngresoProductoTanqueSerializer

    filterset_fields = {
        "ingreso_producto": ["exact"],
    }



