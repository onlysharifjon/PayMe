from rest_framework import serializers
from .models import *


class QiynSerializer(serializers.Serializer):
    phone = serializers.IntegerField()
    password = serializers.CharField(max_length=30)

class OsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymeUser
        fields = '__all__'


class KartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCard
        fields = '__all__'