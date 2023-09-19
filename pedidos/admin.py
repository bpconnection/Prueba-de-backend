from django.contrib import admin

# Register your models here.
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    exclude = ('late_date',)
    list_display = ('username', 'text', 'ttl')
