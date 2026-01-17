from django.db import models

class RegisterUser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    accesslevel = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Item(models.Model):
    itemname = models.CharField(max_length=255)
    description = models.TextField(default="")

    def __str__(self):
        return self.itemname

class Suppliers(models.Model):
    suppliername = models.CharField(max_length=255)
    address = models.TextField(default="")

    def __str__(self):
        return self.suppliername

class Inventory(models.Model):
    item = models.CharField(max_length=255)
    supplier = models.TextField()
    qty = models.IntegerField()
    cost = models.FloatField()
    selling = models.FloatField(default=0)
    date = models.CharField(max_length=255)
    staff = models.CharField(max_length=255)

    def __str__(self):
        return self.item

class Sales(models.Model):
    item = models.CharField(max_length=255)
    qty = models.FloatField()
    price = models.FloatField()
    total = models.FloatField()
    amount = models.FloatField(default=0)
    mop = models.CharField(max_length=255, default="")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item

class Expense(models.Model):
    expensename = models.CharField(max_length=255)
    expenseamount = models.FloatField()
    expensestaff = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.expensename
    
class Price(models.Model):
    itemname = models.CharField()
    price = models.FloatField(default=0)

    def __str__(self):
        return self.itemname