from django import forms
from .models import GuestOrder, Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = GuestOrder
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']


