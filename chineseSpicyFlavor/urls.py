from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views

app_name = 'chineseSpicyFlavor'

urlpatterns = [

    re_path(r'^customerView/$', views.customerView, name='customerView'),
    path('', views.covidWarning, name='covidWarning'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('myOrders/', views.order_list, name='myOrders'),
    path('myOrders/<int:pk>/details', views.order_detail, name='OrderDetail'),
    path('myOrders/<int:pk>/delete', views.order_delete, name='OrderDelete'),
    # path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done.html'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm.html'),
    path('foods/', views.product_list, name='product_list'),
    path('foods/<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('foods/<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('edit/', views.edit, name='edit'),
    path('address/', views.display_addresses, name="displayAddresses"),
    path('address/<int:pk>/edit/', views.address_edit, name='address_edit'),
    path('address/create/', views.address_new, name='address_new'),
    path('address/<int:pk>/delete', views.address_delete, name='address_delete'),
    path('orders/', views.ViewAllOrders.as_view(), name='ViewAllOrders'),
    path('orders/<int:pk>/details', views.AdminOrderDetail, name='AdminOrderDetail'),
    path('orders/<int:pk>/delete', views.AdminOrderDelete, name='AdminOrderDelete'),
    path('sales/', views.Sales.as_view(), name='Sales'),
    path('customers/', views.Customers.as_view(), name='Customers')

]
