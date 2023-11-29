from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from operacional.models import CalidadTanque


class CalidadTanqueSerializer(serializers.ModelSerializer):
    tipo_muestra_nombre = ReadOnlyField(source='tipo_muestra.nombre')
    class Meta:
        model = CalidadTanque
        fields = '__all__'

