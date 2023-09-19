from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderSimpleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField()