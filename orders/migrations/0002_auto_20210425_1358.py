# Generated by Django 3.1.5 on 2021-04-25 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(blank=True, default='226914', editable=False, max_length=6, primary_key=True, serialize=False, unique=True),
        ),
    ]
