from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from operacional.models import Planta

class PlantaSerializer(serializers.ModelSerializer):
    proveedor_nombre = ReadOnlyField(source='proveedor.nombre')
    class Meta:
        model = Planta
        fields = '__all__'


