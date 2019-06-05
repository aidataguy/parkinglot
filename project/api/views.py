from django.contrib.auth.models import User
from api.models import Parking
from api.serializers import UserSerializer, ParkingSerializer
from rest_framework import generics
from rest_framework.response import Response



class ShowUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListParking(generics.ListCreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

