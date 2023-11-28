from rest_framework.viewsets import ModelViewSet

from operacional.api.serializer.ingreso_producto_serializer import IngresoProductoSerializer

from operacional.models import IngresoProducto


class IngresoProductoViewSet(ModelViewSet):
    queryset = IngresoProducto.objects.all()
    serializer_class = IngresoProductoSerializer


