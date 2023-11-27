from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import TipoMuestra, Calidad

class TipoMuestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMuestra
        fields = '__all__'


class CalidadSerializer(serializers.ModelSerializer):
    tipo_muestra_nombre = ReadOnlyField(source='tipo_muestra.nombre')
    class Meta:
        model = Calidad
        fields = '__all__'

