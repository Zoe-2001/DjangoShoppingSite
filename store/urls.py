from django.urls import path
from store import views

urlpatterns = [
    path('login', views.login_action, name='login'),
    path('register', views.register_action, name='register'),
    path('logout', views.logout_action, name='logout'),
    path('mainpage', views.mainpage_action, name='mainpage'),
    path('cart', views.cart, name='cart'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('update_cart', views.update_cart, name='update_cart'),
    path('remove_from_cart', views.remove_from_cart, name='remove_from_cart'),
    path('increase_quantity/<int:cart_item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:cart_item_id>/', views.decrease_quantity, name='decrease_quantity'),
]