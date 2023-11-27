from rest_framework.viewsets import ModelViewSet

from .serializers import PlantaSerializer, ProductoSerializer, ProveedorSerializer, IngresoProductoSerializer, TipoIngresoSerializer

from .models import Planta, Producto, Proveedor, IngresoProducto, TipoIngreso


class PlantaViewSet(ModelViewSet):
    queryset = Planta.objects.all().select_related('proveedor')
    serializer_class = PlantaSerializer


class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProveedorViewSet(ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class IngresoProductoViewSet(ModelViewSet):
    queryset = IngresoProducto.objects.all()
    serializer_class = IngresoProductoSerializer


class TipoIngresoViewSet(ModelViewSet):
    queryset = TipoIngreso.objects.all()
    serializer_class = TipoIngresoSerializer

