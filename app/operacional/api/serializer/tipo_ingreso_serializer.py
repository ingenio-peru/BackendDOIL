from rest_framework import serializers

from operacional.models import TipoIngreso



class TipoIngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIngreso
        fields = '__all__'


