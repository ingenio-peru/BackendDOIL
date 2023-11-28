from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from django.db.models import Sum

from operacional.models import Tanque


class TanqueSerializer(serializers.ModelSerializer):
    tipo_tanque_nombre = ReadOnlyField(source='tipo_tanque.nombre')
    class Meta:
        model = Tanque
        fields = '__all__'

    def create(self, validated_data):
        if validated_data.get('capacidad') is not None:
            validated_data["capacidad_disponible"] = validated_data["capacidad"]
        else:
            validated_data["capacidad_disponible"] = 0
        return super().create(validated_data)


    def update(self, instance, validated_data):
        #calculate capacidad_disponible, capacidad
        if validated_data.get("capacidad") is not None:
            ingresos = instance.ingresoproductotanque_set.filter(tanque=instance).aggregate(Sum("cantidad", default=0)) # {cantidad__sum}
            validated_data["capacidad_disponible"] = validated_data.get("capacidad") - ingresos.get("cantidad__sum", 0)

        return super().update(instance, validated_data)

