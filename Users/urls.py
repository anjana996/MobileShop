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
from  Users.views import registration,signIn,userHome,orderMobile,viewCart,removeCart,viewDetails,logOut,editProfile

urlpatterns =[
    path('admin/', admin.site.urls),
    path('',signIn,name="signin"),
    path('register/',registration,name="register"),
    path('userhome/',userHome,name="userhome"),
    path("order/<int:pk>",orderMobile,name="ordermob"),
    path("cart/",viewCart,name="cart"),
    path("remove/<int:pk>",removeCart,name="remove"),
    path("details/<int:pk>", viewDetails, name="details"),
    path('logout/',logOut,name="logout"),
    path('edit/<int:pk>',editProfile,name='edit')

]