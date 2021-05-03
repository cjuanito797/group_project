from django.db import models
from chineseSpicyFlavor.models import Product, Profile, random, Address


def create_ref_number():
    return str(random.randint(100000, 999999))


class Order(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=6,
        blank=True,
        editable=False,
        unique=True,
        default=create_ref_number()
    )
    profile = models.ForeignKey(Profile,
                                related_name='profile',
                                on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    DELIVERY_CHOICES = (("DELIVERY", 'Delivery'), ("PICKUP", 'Pickup'))
    delivery_pref = models.CharField(max_length=10, choices=DELIVERY_CHOICES, default="Pickup")
    address = models.ForeignKey(Address,
                                unique=False,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)

    class Meta:
        ordering = ('-created',)
        unique_together = (("profile", "id", "created"),)

    def __str__(self):
        return f'{self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE,)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class GuestOrder(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class GuestOrderItem(models.Model):
    guest_order = models.ForeignKey(GuestOrder,
                                    related_name='items',
                                    on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='guestorder_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
