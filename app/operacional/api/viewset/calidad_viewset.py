from rest_framework.viewsets import ModelViewSet

from operacional.models import Calidad
from operacional.api.serializer.calidad_serializer import CalidadSerializer



class CalidadViewSet(ModelViewSet):
    queryset = Calidad.objects.all().select_related('tipo_muestra')
    serializer_class = CalidadSerializer


