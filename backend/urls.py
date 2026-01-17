"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from rest_framework import routers
from kenergy_app.views import RegisterUserView, ItemView, SupplierView, InventoryView, SalesView, SalesViewToday, ExpenseView, ExpenseTodayView, PriceView

router = routers.DefaultRouter()
router.register('registerusers', RegisterUserView, 'registeruser')
router.register('items', ItemView, 'item')
router.register('suppliers', SupplierView, 'supplier')
router.register('inventories', InventoryView, 'inventory')
router.register('sales', SalesView, 'sale')
router.register('sales_today', SalesViewToday, 'sale_today')
router.register('expenses', ExpenseView, 'expense')
router.register('expenses_today', ExpenseTodayView, 'expense_today')
router.register('prices', PriceView, 'price')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]