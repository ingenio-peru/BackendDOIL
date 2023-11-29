from rest_framework.viewsets import ModelViewSet

from operacional.models import CalidadTanque
from operacional.api.serializer.calidad_tanque_serializer import CalidadTanqueSerializer



class CalidadTanqueViewSet(ModelViewSet):
    queryset = CalidadTanque.objects.all().select_related('tipo_muestra')
    serializer_class = CalidadTanqueSerializer

    filterset_fields = {
        "tanque": ["exact"],
    }
