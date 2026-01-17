from rest_framework import serializers
from .models import RegisterUser, Item, Suppliers, Inventory, Sales, Expense, Price

class ReisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RegisterUser

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Item

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Suppliers

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Inventory

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Sales

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Expense

class ExpenseTodaySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Expense

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Price