# Generated by Django 3.1.5 on 2021-04-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20210415_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(blank=True, default='180203', editable=False, max_length=6, primary_key=True, serialize=False, unique=True),
        ),
    ]
