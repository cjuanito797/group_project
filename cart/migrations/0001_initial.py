# Generated by Django 3.1.1 on 2021-05-03 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('key', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=30, null=True)),
            ],
            options={
                'unique_together': {('username', 'key')},
            },
        ),
    ]
