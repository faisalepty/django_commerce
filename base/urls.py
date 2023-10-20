from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('products/', views.Productsd, name='products'),
    path('about/', views.About, name='about'),
    path('register/', views.UserRegistration, name='register'),
    path('login/', views.LoginPage, name='login'),
    path('cart/<str:pk>/', views.CartPage, name='cart'),
    path('cart/<str:pk>/<str:pk2>/', views.CartPage, name='cart2'),
    path('addtocart/<str:pk>/<str:pk2>/', views.AddToCart, name='addtocart'),
    path('delcart/<str:pk>/', views.DelCart, name='delcart'),
    path('logout', views.LogoutPage, name='logout'),
]