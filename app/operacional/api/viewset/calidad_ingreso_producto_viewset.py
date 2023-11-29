from rest_framework.viewsets import ModelViewSet

from operacional.models import CalidadIngresoProducto
from operacional.api.serializer.calidad_ingreso_producto_serializer import CalidadIngresoProductoSerializer



class CalidadIngresoProductoViewSet(ModelViewSet):
    queryset = CalidadIngresoProducto.objects.all().select_related('tipo_muestra')
    serializer_class = CalidadIngresoProductoSerializer

    filterset_fields = {
        "ingreso_producto": ["exact"],
    }
