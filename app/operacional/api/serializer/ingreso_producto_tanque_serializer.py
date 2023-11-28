from rest_framework import serializers, validators

from operacional.models import IngresoProductoTanque



class IngresoProductoTanqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngresoProductoTanque
        fields = '__all__'

    
    def create(self, validated_data):
        if validated_data.get("tanque") is not None and validated_data.get("ingreso_producto"):
            #check ingreso_producto
            
            ingreso = validated_data.get("ingreso_producto")
            if ingreso.peso_neto_disponible < validated_data.get("cantidad"):
                raise validators.ValidationError({"error": "La cantidad supero el peso bruto disponible"})
            tanque = validated_data.get("tanque")
            if tanque.capacidad_disponible < validated_data.get("cantidad"):
                raise validators.ValidationError({"error": "La cantidad supero la cantidad disponible del tanque"})
        instance = super().create(validated_data)
        if instance.tanque_id:
            tanque = instance.tanque
            tanque.capacidad_disponible -= instance.cantidad
            tanque.save()
        if instance.ingreso_producto_id:
            ingreso_producto = instance.ingreso_producto
            ingreso_producto.peso_neto_disponible -= instance.cantidad
            ingreso_producto.save()

        return instance


