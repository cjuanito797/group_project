# Generated by Django 3.1.5 on 2021-04-30 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chineseSpicyFlavor', '0011_auto_20210407_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('braintree_id', models.CharField(blank=True, max_length=150)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(blank=True, default='428723', editable=False, max_length=6, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
                ('braintree_id', models.CharField(blank=True, max_length=150)),
                ('delivery_pref', models.CharField(choices=[('DELIVERY', 'Delivery'), ('PICKUP', 'Pickup')], default='Pickup', max_length=10)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chineseSpicyFlavor.address')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='chineseSpicyFlavor.profile')),
            ],
            options={
                'ordering': ('-created',),
                'unique_together': {('profile', 'id')},
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='chineseSpicyFlavor.product')),
            ],
        ),
        migrations.CreateModel(
            name='GuestOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('guest_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.guestorder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guestorder_items', to='chineseSpicyFlavor.product')),
            ],
        ),
    ]
