from casino_finder.models import Casino
from rest_framework import serializers

class CasinoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Casino
        fields = ('id', 'name', 'address', 'location')
        read_only_fields = ('location', )