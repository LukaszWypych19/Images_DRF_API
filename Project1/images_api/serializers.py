from rest_framework import serializers
from .models import Image, AccountTier


class AccountTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTier
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    account_tier = AccountTierSerializer(read_only=True)

    class Meta:
        model = Image
        fields = '__all__'
