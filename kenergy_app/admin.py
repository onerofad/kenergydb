from django.contrib import admin
from .models import RegisterUser, Price, Item, Inventory, Suppliers, Sales, Expense

admin.site.register({RegisterUser, Price, Item, Inventory, Suppliers, Sales, Expense})
