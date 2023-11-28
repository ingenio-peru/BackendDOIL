from rest_framework.viewsets import ModelViewSet

from operacional.api.serializer.tipo_ingreso_serializer import TipoIngresoSerializer

from operacional.models import Planta, Producto, Proveedor, IngresoProducto, TipoIngreso


class TipoIngresoViewSet(ModelViewSet):
    queryset = TipoIngreso.objects.all()
    serializer_class = TipoIngresoSerializer

