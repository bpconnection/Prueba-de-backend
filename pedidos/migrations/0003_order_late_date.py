# Generated by Django 4.2.5 on 2023-09-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_alter_order_ttl'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='late_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]