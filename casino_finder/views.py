from casino_finder.models import Casino
from casino_finder.serializers import CasinoSerializers
from rest_framework import generics


class ListCreateCasinos(generics.ListCreateAPIView):
    queryset = Casino.objects.all()
    serializer_class = CasinoSerializers