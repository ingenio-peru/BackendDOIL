from rest_framework.viewsets import ModelViewSet

from operacional.api.serializer.proveedor_serializer import ProveedorSerializer

from operacional.models import Proveedor


class ProveedorViewSet(ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


