from django.contrib import admin
from django.urls import path


from accounts import views

urlpatterns = [
    path('', views.home, name="home"),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/',views.userpage, name="user"),
    path('account/', views.accountSettings, name="account"),

    path('products/', views.products, name="products"),
    path('customers/<str:pk>/', views.customers, name="customers"),

    path('createorder/<str:pk>/', views.createOrder, name="createOrder"),
    path('updateorder/<str:pk>/', views.updateOrder, name="updateOrder"),
    path('deleteorder/<str:pk>/', views.deleteOrder, name="deleteOrder"),

]
