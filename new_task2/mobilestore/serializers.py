from rest_framework import serializers
from .models import Mobile, CartItem


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ['id', 'model', 'stock']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'mobile', 'quantity']
