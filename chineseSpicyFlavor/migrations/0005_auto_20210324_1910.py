# Generated by Django 3.1.7 on 2021-03-25 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chineseSpicyFlavor', '0004_auto_20210310_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.CharField(blank=True, default='308042', editable=False, max_length=6, primary_key=True, serialize=False, unique=True),
        ),
    ]
