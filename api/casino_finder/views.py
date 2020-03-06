from casino_finder.models import Casino
from casino_finder.serializers import CasinoSerializers
from rest_framework import generics
import geocoder

class ListCreateCasinos(generics.ListCreateAPIView):
    queryset = Casino.objects.all()
    serializer_class = CasinoSerializers

    def perform_create(self, serializer):
        address = serializer.initial_data['address']
        g = geocoder.google(address)
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        pnt = 'POINT(' + str(longitude) + ' ' + str(latitude) + ')'
        serializer.save(location=pnt)