from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views

app_name = 'chineseSpicyFlavor'

urlpatterns = [
    path('', views.covidWarning, name='covidWarning'),
    re_path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('customerView/', views.customerView, name='customerView'),
    path('myOrders/', views.order_list, name='myOrders'),
    path('myOrders/<int:pk>/details', views.order_detail, name='OrderDetail'),
    # path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('foods/', views.product_list, name='product_list'),
    path('foods/<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('foods/<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('menu/', views.menu, name='menu'),
    path('edit/', views.edit, name='edit'),
    path('address/', views.display_addresses, name="displayAddresses"),
    path('address/<int:pk>/edit/', views.address_edit, name='address_edit'),
    path('address/create/', views.address_new, name='address_new'),
    path('address/<int:pk>/delete', views.address_delete, name='address_delete'),

]
