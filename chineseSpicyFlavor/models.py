import random
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d',
                              blank=True)
    streetNum = models.CharField(max_length=25)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return f'Profile for user {self.user.username}'


def create_new_ref_number():
    return str(random.randint(100000, 999999))


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True,
                            default='someValue')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chineseSpicyFlavor:item_list',
                       args=[self.slug])


class Item(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='items',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, default='someValue')
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chineseSpicyFlavor:item_list',
                       args=[self.id, self.slug])


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)


class Order(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=6,
        blank=True,
        editable=False,
        unique=True,
        default=create_new_ref_number()
    )
    orderQty = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now=True)
    deliveryChoices = (
        ('delivery', 'Delivery'),
        ('pickup', 'Pickup')
    )

    customer = models.ForeignKey(Profile, db_column="Profile", on_delete=models.CASCADE)

    deliveryPref = models.CharField(max_length=10,
                                    choices=deliveryChoices,
                                    default='pickup')

    class Meta:
        ordering = ('id',)
        managed = True

    def __str__(self):
        """String representation for an order object"""
        return f'{self.id}'
