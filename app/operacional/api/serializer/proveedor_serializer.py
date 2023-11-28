from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from operacional.models import Planta, Producto, Proveedor, IngresoProducto, TipoIngreso


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


