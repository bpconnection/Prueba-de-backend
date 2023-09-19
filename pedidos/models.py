from django.db import models

# Create your models here.

from django.utils import timezone

class Order(models.Model):
    username = models.CharField(max_length=255, blank=False)  # Campo obligatorio
    text = models.TextField(blank=False)  # Campo obligatorio
    ttl = models.IntegerField(default=60,blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)  # Utiliza timezone.now()
    late_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'

    def __str__(self):
        return f"Order de {self.username}"

    def save(self, *args, **kwargs):
        if self.ttl is None:
            self.ttl = 60  # Establece el valor predeterminado de 60 si ttl no tiene un valor
        super().save(*args, **kwargs)