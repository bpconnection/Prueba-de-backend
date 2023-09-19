from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer,OrderSimpleSerializer
from datetime import datetime, timedelta
from django.utils import timezone  # Importa timezone desde django.utils

@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"id": serializer.data['id']}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_order_by_id(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

        # Calcular la fecha y hora en que la orden se considera tarde
    created_at = order.created_at
    ttl = order.ttl
    late_date = created_at + timedelta(seconds=ttl)

    # Crear manualmente la respuesta JSON con los campos deseados
    data = {
        "username": order.username,
        "text": order.text,
        "late_date": late_date.isoformat(),
    }

    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_order_by_user(request, username):
    # Obtener todas las órdenes para el nombre de usuario dado que aún no están consideradas tarde
    ahora = timezone.now()
    orders = Order.objects.filter(username=username, late_date__isnull=True)

    # Calcular y marcar las órdenes como tardías si corresponde
    for order in orders:
        if order.created_at + timedelta(seconds=order.ttl) < ahora:
            order.late_date = ahora
            order.save()

    # Utiliza el nuevo serializador personalizado para mostrar solo los campos 'id' y 'text'
    serializer = OrderSimpleSerializer(orders, many=True)  # Usa el serializador personalizado

    # Crear la respuesta JSON
    data = serializer.data

    return Response(data, status=status.HTTP_200_OK)
