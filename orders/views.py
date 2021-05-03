from django.urls import reverse
from django.shortcuts import render, redirect
from .models import OrderItem, GuestOrderItem
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order, GuestOrder
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from chineseSpicyFlavor.models import Profile, Address
from chineseSpicyFlavor.views import display_addresses
from .forms import OrderCreateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import random


def create_ref_number():
    return str(random.randint(100000, 999999))


# import weasyprint

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\
        "order_{}.pdf"'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(
                                               settings.STATIC_ROOT + 'css/pdf.css')])
    return response


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})


def create_order(request):
    cart = Cart(request)
    if request.user.is_authenticated:
        addresses = Address.objects.filter(user_id=request.user)
        if request.method == 'POST':
            if 'place_order' in request.POST:
                myVar = request.POST.get("address")
                address = Address.objects.get(pk=myVar)
                # create a dummy order object to store in database
                new_order = Order.objects.create(
                    id=create_ref_number(),
                    profile_id=request.user.id,
                    delivery_pref='Delivery',
                    address_id=myVar

                )

                for item in cart:
                    OrderItem.objects.create(order=new_order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                cart.clear()

                # Redirect for the payment
                request.session['user_order_id'] = new_order.id
                return redirect(reverse('payment:process'))

            elif 'pickup_order' in request.POST:

                print(request.user.id)
                new_order = Order.objects.create(
                    id=create_ref_number(),
                    profile_id=request.user.id,
                    delivery_pref='PICKUP',
                    address=None

                )
                for item in cart:
                    OrderItem.objects.create(order=new_order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                cart.clear()

                # Redirect for the payment
                request.session['user_order_id'] = new_order.id
                return redirect(reverse('payment:process'))

        else:
            return render(request,
                          'orders/order/create.html',
                          {'cart': cart, 'addresses': addresses})
    else:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    GuestOrderItem.objects.create(guest_order=order,
                                                  product=item['product'],
                                                  price=item['price'],
                                                  quantity=item['quantity'])
                # clear the cart
                cart.clear()
                # set the order in the session
                request.session['order_id'] = order.id

                # Redirect for the payment
                return redirect(reverse('payment:process'))

        else:
            form = OrderCreateForm()
        return render(request,
                      'orders/order/guest_orderCreate.html',
                      {'cart': cart, 'form': form})
