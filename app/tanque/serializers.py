from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import TipoTanque, Tanque

class TipoTanqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTanque
        fields = '__all__'

class TanqueSerializer(serializers.ModelSerializer):
    tipo_tanque_nombre = ReadOnlyField(source='tipo_tanque.nombre')
    class Meta:
        model = Tanque
        fields = '__all__'

