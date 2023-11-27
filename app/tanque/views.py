from rest_framework.viewsets import ModelViewSet

from .models import TipoTanque, Tanque
from .serializers import TipoTanqueSerializer, TanqueSerializer

class TipoTanqueViewSet(ModelViewSet):
    queryset = TipoTanque.objects.all()
    serializer_class = TipoTanqueSerializer


class TanqueViewSet(ModelViewSet):
    queryset = Tanque.objects.all().select_related('tipo_tanque')
    serializer_class = TanqueSerializer
