from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import RegisterUser, Item, Suppliers, Inventory, Sales, Expense, Price
from .serializers import ReisterUserSerializer, ItemSerializer, SupplierSerializer, InventorySerializer, SaleSerializer, ExpenseSerializer, ExpenseTodaySerializer, PriceSerializer
from datetime import date

class RegisterUserView(viewsets.ModelViewSet):
    queryset = RegisterUser.objects.all()
    serializer_class = ReisterUserSerializer

class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class SupplierView(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SupplierSerializer

class InventoryView(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class SalesView(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SaleSerializer

class SalesViewToday(viewsets.ModelViewSet):
    queryset = Sales.objects.filter(date = date.today())
    serializer_class = SaleSerializer

class ExpenseView(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseTodayView(viewsets.ModelViewSet):
    queryset = Expense.objects.filter(date = date.today())
    serializer_class = ExpenseTodaySerializer

class PriceView(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer



