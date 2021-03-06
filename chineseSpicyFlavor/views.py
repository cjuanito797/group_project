from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib import messages
from .models import Item, Order, Category, Profile


def item_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    items = Item.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)

    return render(request,
                  'items/list.html',
                  {'category': category,
                   'categories': categories,
                   'items': items})


# Create your views here.
def home(request):
    num_orders = Order.objects.all()
    context = {
        'num_orders': num_orders
    }
    # Render the html template home.html with the data in the context variable
    return render(request, 'home.html', context=context)


def order_now(request):
    return render(request, 'order_now.html')


def covidWarning(request):
    return render(request, 'covidPrec.html')


def menu(request):
    return render(request, 'menu.html')


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
    return render(request, 'account/base.html')


from .forms import UserEditForm, ProfileEditForm


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


# Create a view that allows user to edit delivery preferences
from .forms import DeliveryEditForm


@login_required
def editDeliveryPref(request):
    if request.method == 'POST':
        profile_form = DeliveryEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Delivery Preferences Updated '
                                      'successfully')
            return render(request, 'account/base.html')
        else:
            messages.error(request, 'Error updating your delivery preferences')
    else:
        profile_form = DeliveryEditForm(
            instance=request.user.profile)
    return render(request,
                  'account/edit_delivery.html',
                  {
                      'profile_form': profile_form})
