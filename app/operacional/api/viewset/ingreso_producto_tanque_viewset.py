from rest_framework.viewsets import ModelViewSet

from django.db import transaction

from operacional.api.serializer.ingreso_producto_tanque_serializer import IngresoProductoTanqueSerializer

from operacional.models import IngresoProductoTanque


class IngresoProductoTanqueViewSet(ModelViewSet):
    queryset = IngresoProductoTanque.objects.all()
    serializer_class = IngresoProductoTanqueSerializer

    filterset_fields = {
        "tanque": ["exact"],
        "ingreso_producto": ["exact"],
        "fecha": ["gte", "gt", "lt", "lte", "exact"],
    }

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


