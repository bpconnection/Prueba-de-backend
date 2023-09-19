from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.create_order, name='order'),
    path('order/<int:order_id>/', views.get_order_by_id, name='obtener_orden_por_id'),
    path('orders/<str:username>/', views.get_order_by_user, name='obtener_ordenes_por_usuario'),
]