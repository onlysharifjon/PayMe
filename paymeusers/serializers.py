from rest_framework import serializers
from .models import *


class QiynSerializer(serializers.Serializer):
    phone = serializers.IntegerField()
    password = serializers.CharField(max_length=30)


class OsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymeUser
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    # class Meta:
    #     model = PaymeUser
    #     fields = ('name', 'phone')
    name = serializers.CharField(max_length=255)
    phone = serializers.IntegerField()
    new_password = serializers.CharField(max_length=16)
    confirm_password = serializers.CharField(max_length=16)


class KartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCard
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCard
        fields = ('number',)


class DeleteCardSerializer(serializers.Serializer):
    # class Meta:
    #     model = BaseCard
    #     fields = ('number',)
    card_number = serializers.CharField(max_length=16)


class DeletePaymeuserSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField()


class Transaction(serializers.Serializer):
    card_sender = serializers.CharField(max_length=16)
    card_getter = serializers.CharField(max_length=16)
    money = serializers.IntegerField()


class HistoryTransactions(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'
