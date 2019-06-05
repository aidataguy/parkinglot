from api.models import User, Parking
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__' )

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ('__all__' )