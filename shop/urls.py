from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name="product_list"),
    path('add/', views.product_create, name="product_create"),
    path('edit/<int:pk>/', views.product_update, name="product_update"),
    path('delete/<int:pk>/', views.product_delete, name="product_delete"),

    # cart urls
    path('cart/', views.cart_detail, name="cart_detail"),
    path('cart/add/<int:pk>/', views.add_to_cart, name="add_to_cart"),
    path('cart/increase/<int:pk>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:pk>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name="remove_from_cart"),
    path('cart/clear/', views.clear_cart, name="clear_cart"),
]
