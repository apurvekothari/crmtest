# Generated by Django 3.0.4 on 2020-04-03 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200403_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
