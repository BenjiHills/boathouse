# Generated by Django 4.0.1 on 2022-02-28 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0017_alter_order_customer_alter_order_dessert_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(db_constraint=False, default=3203561428832, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PE', 'Pending'), ('DE', 'Out for Delivery'), ('CO', 'Order Complete')], default='OR', max_length=2),
        ),
    ]
