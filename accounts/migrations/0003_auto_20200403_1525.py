# Generated by Django 3.0.4 on 2020-04-03 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_orders_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Customers'),
        ),
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Products'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
