from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_list_view, name='product_list'),
    path('products/<int:pk>/', views.product_detail_view, name='product_detail'),
    path('products/upload/', views.product_upload_view, name='product_upload'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/add/<int:pk>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:pk>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
