from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from operacional.models import Calidad


class CalidadSerializer(serializers.ModelSerializer):
    tipo_muestra_nombre = ReadOnlyField(source='tipo_muestra.nombre')
    class Meta:
        model = Calidad
        fields = '__all__'

