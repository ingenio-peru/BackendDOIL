from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from operacional.models import CalidadIngresoProducto


class CalidadIngresoProductoSerializer(serializers.ModelSerializer):
    tipo_muestra_nombre = ReadOnlyField(source='tipo_muestra.nombre')
    class Meta:
        model = CalidadIngresoProducto
        fields = '__all__'

