# Generated by Django 4.0.1 on 2022-03-05 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0028_alter_order_customer_alter_order_dessert_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='descrip',
            field=models.TextField(blank=True, max_length=150, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=2468437707728, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='dessert',
            field=models.ForeignKey(default=2468395942128, limit_choices_to={'course': 'EM'}, on_delete=django.db.models.deletion.CASCADE, related_name='dessert', to='menu.dish'),
        ),
        migrations.AlterField(
            model_name='order',
            name='main',
            field=models.ForeignKey(default=2468395942128, limit_choices_to={'course': 'EM'}, on_delete=django.db.models.deletion.CASCADE, related_name='main', to='menu.dish'),
        ),
        migrations.AlterField(
            model_name='order',
            name='starter',
            field=models.ForeignKey(default=2468395942128, limit_choices_to={'course': 'EM'}, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='starter', to='menu.dish'),
        ),
    ]