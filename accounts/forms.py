from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Orders, Customers


class OrderForm(ModelForm):
    class Meta:  # A metaclass is a class whose instance is a class.
        model = Orders  # providing model class for which we are creating form
        fields = '__all__'  # create models of all field present in Orders model class


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(ModelForm):
	class Meta:
		model = Customers
		fields = '__all__'
		exclude = ['user']

