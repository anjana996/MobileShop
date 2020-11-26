"""MobileShopOnline URL Configuration

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
from shopowner.views import createBrand,viewBrand,updateBrand,createMobile,listMobile,mobileView,mobileDelete,updateMobile,deleteBrand,viewOrders,orderdetails,index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('listbrand',listBrand,name='listbrand'),
    path('createbrand',createBrand,name="createbrand"),
    path('viewbrand/<int:pk>',viewBrand,name="viewbrand"),
    path('deletebrand/<int:pk>',deleteBrand,name="deletebrand"),
    path('updatebrand/<int:pk>', updateBrand, name="updatebrand"),
    path('listmobile', listMobile, name="listmobile"),

    path('createmob',createMobile,name="createmobile"),
    path('viewmobile/<int:pk>',mobileView,name="viewmobile"),
    path('mobdelete/<int:pk>', mobileDelete, name="deletemobile"),
    path('mobupdate/<int:pk>',updateMobile, name="mobileupdate"),
    path('vieworders',viewOrders,name="vieworders"),
    path('orderdetails/<int:pk>',orderdetails,name="orderdetails"),
    path('index/',index,name="index")

]
