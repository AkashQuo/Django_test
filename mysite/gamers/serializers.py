from rest_framework import serializers
from .models import GAMER_USER

class GamerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GAMER_USER
        fields = '__all__'
