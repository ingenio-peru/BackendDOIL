from rest_framework.viewsets import ModelViewSet

from operacional.models import TipoTanque, Tanque
from operacional.api.serializer.tipo_tanque_serializer import TipoTanqueSerializer

class TipoTanqueViewSet(ModelViewSet):
    queryset = TipoTanque.objects.all()
    serializer_class = TipoTanqueSerializer

