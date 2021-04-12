from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.contrib import messages
from .models import Product, Category, Profile, Address
from orders.models import Order, OrderItem
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .forms import AddressForm
from django.http import HttpResponse


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


# Create your views here.
def home(request):
    # Render the html template home.html with the data in the context variable
    return render(request, 'home.html')


def order_now(request):
    return render(request, 'order_now.html')


def covidWarning(request):
    return render(request, 'covidPrec.html')


def menu(request):
    return render(request, 'menu.html')


def entrees(request):
    return render(request, 'entrees.html')


def sides(request):
    return render(request, 'sides.html')


def drinks(request):
    return render(request, 'drinks.html')


def desserts(request):
    return render(request, 'desserts.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'home.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'Registration/login.html', {'form': form})


from django.contrib.auth.decorators import login_required


@login_required
def customerView(request):
    request.session.set_test_cookie()
    orders = Order.objects.filter()
    orderItem = OrderItem.objects.all()
    return render(request, 'account/base.html')


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated '
                                      'successfully')
            return render(request, 'account/base.html')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


from .forms import LoginForm, UserRegistrationForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'Registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'Registration/register.html',
                  {'user_form': user_form})


# Create a prototype view that displays the user's addresses on file
@login_required
def display_addresses(request):
    addresses = Address.objects.filter(user_id=request.user)
    return render(request, 'account/addresses.html', {'addresses': addresses})


@login_required
def sample_view(request):
    current_user = request.user
    return render(request, 'account/sample.html', {'current_user': current_user})


@login_required
def address_new(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            addresses = Address.objects.filter(user_id=request.user)
            messages.success(request, 'Address Added '
                                      'successfully')
            return render(request, 'account/base.html')
    else:
        form = AddressForm()
    return render(request, 'account/address_new.html', {'form': form})


@login_required
def address_edit(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save()
            # service.customer = service.id
            address.save()
            addresses = Address.objects.all()
            return render(request, 'account/addresses.html', {'addresses': addresses})
    else:
        # print("else")
        form = AddressForm(instance=address)
    return render(request, 'account/address_edit.html', {'form': form})


@login_required()
def address_delete(request, pk):
    address = get_object_or_404(Address, pk=pk)
    address.delete()
    return redirect('chineseSpicyFlavor:displayAddresses')


@login_required
def order_list(request):
    request.session.test_cookie_worked()
    orders = Order.objects.filter(profile__user_id=request.user)
    return render(request, 'account/order_list.html', {'orders': orders})


@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('chineseSpicyFlavor:myOrders')


@login_required
def order_detail(request, pk):
    order_instance = get_object_or_404(Order, pk=pk)
    orderItems = OrderItem.objects.filter(order=order_instance)

    return render(request, 'account/order_detail.html', {'order_instance': order_instance, 'orderItems': orderItems})


def about(request):
    return render(request, 'about.html')


@login_required
def user_logout(request):
    try:
        for key in list(request.session.keys()):
            if key == 'CART':
                continue
            del request.session[key]
    except KeyError:
        pass
    return HttpResponseRedirect(reversed('your_app:login'))
