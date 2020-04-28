from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from django.forms import inlineformset_factory  # create multiple form in one form
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticatedUser, allowedUsers, adminOnly
from django.contrib.auth.models import Group


@login_required(login_url='login')
@adminOnly
def home(request):
    ordersList = Orders.objects.all()
    customersList = Customers.objects.all()
    total_customers = customersList.count()
    total_orders = ordersList.count()
    delivered = ordersList.filter(status="Delivered").count()
    pending = ordersList.filter(status="Pending").count()
    context = {'orderList': ordersList, 'customersList': customersList, 'total_orders': total_orders,
               'delivered': delivered, 'pending': pending}

    return render(request, "accounts/dashboard.html", context)


@login_required(login_url='login')
# @allowedUsers(allowed_roles=['customer'])
def userpage(request):
    orders = request.user.customers.orders_set.all()
    print(orders)
    context = {'orders': orders}
    return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
@allowedUsers(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customers
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form }
    return render(request, 'accounts/account_settings.html', context)


@unauthenticatedUser
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            # Added username after video because of error returning customer name if not added
            Customers.objects.create(
                user=user,
                name=user.username,
            )

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticatedUser
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print("in Login view")
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowedUsers(allowed_roles=['admin'])
def products(request):
    products = Products.objects.all()
    return render(request, "accounts/products.html", {'productsList': products})


@login_required(login_url='login')
@allowedUsers(allowed_roles=['admin'])
def customers(request, pk):
    customers = Customers.objects.get(id=pk)
    order = customers.orders_set.all()
    totalOrder = order.count()
    myFilter = OrderFilter(request.GET, queryset=order)
    order = myFilter.qs
    context = {'customer': customers, 'order': order, 'totalOrder': totalOrder, 'myFilter': myFilter}
    return render(request, "accounts/customers.html", context)


@login_required(login_url='login')
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customers, Orders, fields=('product', 'status'), extra=10)
    customers = Customers.objects.get(id=pk)
    formset = OrderFormSet(queryset=Orders.objects.none(), instance=customers)
    # form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customers)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form': formset}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
def updateOrder(request, pk):
    orders = Orders.objects.get(id=pk)
    form = OrderForm(instance=orders)  # pre-filled form we can see
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()  # save data in database
            return redirect('/')

    context = {'form': form}
    return render(request, "accounts/order_form.html", context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    orders = Orders.objects.get(id=pk)
    if request.method == "POST":
        orders.delete()
        return redirect('/')

    context = {'item': orders}
    return render(request, 'accounts/delete.html', context)
