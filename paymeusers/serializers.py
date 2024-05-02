from rest_framework import serializers
from .models import PaymeUser


class QiynSerializer(serializers.Serializer):
    phone = serializers.IntegerField()
    password = serializers.CharField(max_length=30)

class OsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymeUser
        fields = '__all__'
