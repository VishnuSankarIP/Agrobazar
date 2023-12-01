"""agrobazarproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from agrobazarapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    
    path('farmerreg', views.farmerreg, name='farmerreg'),
    path('farmerregshow', views.farmerregshow, name='farmerregshow'),
    path('deliveryboyreg', views.deliveryboyreg, name='deliveryboyreg'),
    path('deliveryboyregshow', views.deliveryboyregshow, name='deliveryboyregshow'),
    path('customerreg', views.customerreg, name='customerreg'),
    path('customerregshow', views.customerregshow, name='customerregshow'),
    path('login', views.login, name='login'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('farmerhome', views.farmerhome, name='farmerhome'),
    path('deliveryboyhome', views.deliveryboyhome, name='deliveryboyhome'),
    path('customerhome', views.customerhome, name='customerhome'),
    path('approvefarmer', views.approvefarmer, name='approvefarmer'),
    path('approvedeliveryboy', views.approvedeliveryboy, name='approvedeliveryboy'),
    path('approvecustomer', views.approvecustomer, name='approvecustomer'),
    
    path('deletefarmer', views.deletefarmer, name='deletefarmer'),
    path('deletedeliveryboy', views.deletedeliveryboy, name='deletedeliveryboy'),
    path('deletecustomer', views.deletecustomer, name='deletecustomer'),
    path('selectfarmer', views.selectfarmer, name='selectfarmer'),
    path('selectdeliveryboy', views.selectdeliveryboy, name='selectdeliveryboy'),
    path('selectcustomer', views.selectcustomer, name='selectcustomer'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('viewaddproduct', views.viewaddproduct, name='viewaddproduct'),
    path('adminviewaddproduct', views.adminviewaddproduct, name='adminviewaddproduct'),
    path('customerviewproduct', views.customerviewproduct, name='customerviewproduct'),
    path('insertintocart', views.insertintocart, name='insertintocart'),
    path('viewcartproduct', views.viewcartproduct, name='viewcartproduct'),
    path('selectorder', views.selectorder, name='selectorder'),
    path('feedback', views.feedback, name='feedback'),
    path('viewfeedback', views.viewfeedback, name='viewfeedback'),
    path('selectfeedback', views.selectfeedback, name='selectfeedback'),
    path('viewdeliveryboy', views.viewdeliveryboy, name='viewdeliveryboy'),
    path('assigndeliveryboy', views.assigndeliveryboy, name='assigndeliveryboy'),
    path('deleteproduct', views.deleteproduct, name='deleteproduct'),
    path('deliveryboyvieworder', views.deliveryboyvieworder, name='deliveryboyvieworder'),
    path('orderdelivered', views.orderdelivered, name='orderdelivered'),
    path('customerviewcart', views.customerviewcart, name='customerviewcart'),
    path('cancelorder', views.cancelorder, name='cancelorder'),
    path('payment', views.payment, name='payment'),
    path('farmerviewpayments', views.farmerviewpayments, name='farmerviewpayments'),
    path('farmerviewdeliverystatus', views.farmerviewdeliverystatus, name='farmerviewdeliverystatus'),
    path('CustomerViewpdttDetails', views.CustomerViewpdttDetails, name='CustomerViewpdttDetails'),
    path('customerviewquick', views.customerviewquick, name='customerviewquick'),
    path('adminviewcart', views.adminviewcart, name='adminviewcart'),
    
    path('adminviewdeliveryboy', views.adminviewdeliveryboy, name='adminviewdeliveryboy'),
    path('deletedboys', views.deletedboys, name='deletedboys'),
    
    
]
