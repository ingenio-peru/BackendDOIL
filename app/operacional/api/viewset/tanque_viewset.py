from rest_framework.viewsets import ModelViewSet

from operacional.models import TipoTanque, Tanque
from operacional.api.serializer.tanque_serializer import TanqueSerializer



class TanqueViewSet(ModelViewSet):
    queryset = Tanque.objects.all().select_related('tipo_tanque')
    serializer_class = TanqueSerializer
