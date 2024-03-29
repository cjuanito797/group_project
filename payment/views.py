import braintree
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import GuestOrder, Order
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
# import weasyprint
from io import BytesIO
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def payment_process(request):
    # Process payment if user is authenticated
    if request.user.is_authenticated:
        order_id = request.session.get('user_order_id')
        order = get_object_or_404(Order, id=order_id)

        if request.method == 'POST':
            # retrieve nonce
            nonce = request.POST.get('payment_method_nonce', None)
            # create and submit transaction
            result = braintree.Transaction.sale({
                'amount': '{:.2f}'.format(order.get_total_cost()),
                'payment_method_nonce': nonce,
                'options': {
                    'submit_for_settlement': True
                }
            })
            if result.is_success:
                # mark the order as paid
                order.paid = True
                # store the unique transaction id
                order.braintree_id = result.transaction.id
                order.save()
                # create invoice e-mail

                return redirect('payment:done')
            else:
                order.paid = False
                order.save()
                return redirect('payment:canceled')
        else:
            # generate token
            client_token = braintree.ClientToken.generate()
            return render(request,
                          'payment/process.html',
                          {'order': order,
                           'client_token': client_token})
    elif (request.user.is_authenticated == False):
        order_id = request.session.get('order_id')
        order = get_object_or_404(GuestOrder, id=order_id)

        if request.method == 'POST':
            # retrieve nonce
            nonce = request.POST.get('payment_method_nonce', None)
            # create and submit transaction
            result = braintree.Transaction.sale({
                'amount': '{:.2f}'.format(order.get_total_cost()),
                'payment_method_nonce': nonce,
                'options': {
                    'submit_for_settlement': True
                }
            })
            if result.is_success:
                # mark the order as paid
                order.paid = True
                # store the unique transaction id
                order.braintree_id = result.transaction.id
                order.save()
                # create invoice e-mail

                return redirect('payment:done')
            else:
                return redirect('payment:canceled')
        else:
            # generate token
            client_token = braintree.ClientToken.generate()
            return render(request,
                          'payment/process.html',
                          {'order': order,
                           'client_token': client_token})



def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
