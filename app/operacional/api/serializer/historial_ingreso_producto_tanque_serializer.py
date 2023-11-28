from rest_framework import serializers

from operacional.models import HistorialIngresoProductoTanque



class HistorialIngresoProductoTanqueSerializer(serializers.ModelSerializer):
    descripcion = serializers.SerializerMethodField()

    class Meta:
        model = HistorialIngresoProductoTanque
        fields = '__all__'

    def get_descripcion(self, instance: HistorialIngresoProductoTanque) -> str:
        if instance.tanque_origen_id:
            return f'Se envio {instance.cantidad} de {instance.tanque_origen.nombre if instance.tanque_origen_id else ""} a {instance.tanque_destino.nombre if instance.tanque_destino_id else ""}'
        return f'Se envio {instance.cantidad} a {instance.tanque_destino.nombre if instance.tanque_destino_id else ""}'

