from rest_framework import serializers
from .models import Account, Customer, Transaction

from drf_writable_nested import WritableNestedModelSerializer

# Fill in fields with information from models.py
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Account
        fields = (
            'pk',
            'account_number',
            'balance',
            'account_status'
        )

class CustomerSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model =  Customer
        fields = (
            'pk',
            'first_name',
            'last_name',
            'account'
        )

class TransactionSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model =  Transaction
        fields = (
            'pk',
            'amount',
            'transaction_type',
            'account'
        )
