from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import Planta, Producto, Proveedor, IngresoProducto, TipoIngreso

class PlantaSerializer(serializers.ModelSerializer):
    proveedor_nombre = ReadOnlyField(source='proveedor.nombre')
    class Meta:
        model = Planta
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


class IngresoProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngresoProducto
        fields = '__all__'


class TipoIngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIngreso
        fields = '__all__'


