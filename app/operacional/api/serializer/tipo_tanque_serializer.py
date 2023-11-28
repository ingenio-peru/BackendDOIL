from rest_framework import serializers

from operacional.models import TipoTanque

class TipoTanqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTanque
        fields = '__all__'



