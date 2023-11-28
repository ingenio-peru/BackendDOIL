from rest_framework import serializers

from operacional.models import TipoMuestra

class TipoMuestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMuestra
        fields = '__all__'



