from rest_framework.viewsets import ModelViewSet

from operacional.api.serializer.planta_serializer import PlantaSerializer

from operacional.models import Planta


class PlantaViewSet(ModelViewSet):
    queryset = Planta.objects.all().select_related('proveedor')
    serializer_class = PlantaSerializer

