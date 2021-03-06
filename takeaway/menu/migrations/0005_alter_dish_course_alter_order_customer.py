# Generated by Django 4.0.1 on 2022-02-27 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='course',
            field=models.CharField(choices=[('ST', 'Starter'), ('MA', 'Main'), ('DE', 'Dessert')], default='ST', max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=1238758806448, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
