from rest_framework.viewsets import ModelViewSet

from .models import TipoMuestra, Calidad
from .serializers import TipoMuestraSerializer, CalidadSerializer


class TipoMuestraViewSet(ModelViewSet):
    queryset = TipoMuestra.objects.all()
    serializer_class = TipoMuestraSerializer


class CalidadViewSet(ModelViewSet):
    queryset = Calidad.objects.all().select_related('tipo_muestra')
    serializer_class = CalidadSerializer


