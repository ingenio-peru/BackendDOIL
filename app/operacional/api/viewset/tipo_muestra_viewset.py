from rest_framework.viewsets import ModelViewSet

from operacional.models import TipoMuestra
from operacional.api.serializer.tipo_muestra_serializer import TipoMuestraSerializer


class TipoMuestraViewSet(ModelViewSet):
    queryset = TipoMuestra.objects.all()
    serializer_class = TipoMuestraSerializer



