from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import *

def home(request):
    ordersList = Orders.objects.all()
    customersList = Customers.objects.all()
    total_customers = customersList.count()
    total_orders = ordersList.count()
    delivered = ordersList.filter(status="Delivered").count()
    pending = ordersList.filter(status="Pending").count()
    context = {'orderList' : ordersList, 'customersList' : customersList, 'total_orders' : total_orders,
               'delivered' : delivered, 'pending' : pending}

    return render(request, "accounts/dashboard.html", context)


def products(request):
    products = Products.objects.all()
    return render(request, "accounts/products.html", {'productsList': products })


def customers(request, pk):
    customers = Customers.objects.get(id=pk)
    order = customers.orders_set.all()
    totalOrder = order.count()
    context = {'customer' : customers,'order' : order, 'totalOrder' : totalOrder}
    return render(request, "accounts/customers.html", context)
