from rest_framework.viewsets import ModelViewSet

from operacional.api.serializer.producto_serializer import ProductoSerializer

from operacional.models import Producto


class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


