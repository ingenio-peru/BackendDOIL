from rest_framework import serializers
from django.db.models import Sum

from operacional.models import IngresoProducto



class IngresoProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngresoProducto
        fields = '__all__'

    def create(self, validated_data):
        #peso_neto, peso_neto_disponible
        if validated_data.get('peso_bruto') is not None and validated_data.get('peso_tara') is not None:
            peso_neto = validated_data.get('peso_bruto') + validated_data.get('peso_tara')
            if peso_neto>=0:
                validated_data["peso_neto"] = peso_neto
                validated_data["peso_neto_disponible"] = peso_neto
            else:
                validated_data["peso_neto"] = 0
                validated_data["peso_neto_disponible"] = 0
        else:
            validated_data["peso_neto"] = 0
            validated_data["peso_neto_disponible"] = 0
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if validated_data.get('peso_bruto') is not None and validated_data.get('peso_tara') is not None:
            if instance.peso_bruto != validated_data["peso_bruto"] or instance.peso_tara != validated_data["peso_tara"]:
                peso_neto = validated_data.get('peso_bruto') + validated_data.get('peso_tara')
                if peso_neto>=0:
                    validated_data["peso_neto"] = peso_neto
                else:
                    peso_neto = 0
                    validated_data["peso_neto"] = 0
                ingresos = instance.ingresoproductotanque_set.filter(ingreso_producto=instance).aggregate(Sum("cantidad", default=0)) # {cantidad__sum}
                validated_data["peso_neto_disponible"] = peso_neto - ingresos.get("cantidad__sum", 0)
        return super().update(instance, validated_data)

