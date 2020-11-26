from django.shortcuts import render, redirect
from Users.forms import RegistrationForm,OrderForm,Order,EditProfile,User
from django.contrib.auth import login,logout,authenticate
from shopowner.models import Mobile
from Users.models import Order

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="signin")
def userHome(request):
    mobile=Mobile.objects.all()
    context={}
    context["mobile"]=mobile
    return render(request,"users/userhome.html",context)
def signIn(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        psswd = request.POST.get("pwd")
        user=authenticate(request,username=username,password=psswd)
        if user is not None:
            login(request,user)
            return redirect("userhome")


    return render(request,"users/login.html")
def logOut(request):
     logout(request)
     return redirect("signin")


def registration(request):
    form=RegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context["form"] = form
            return render(request, "users/registration.html", context)

    return render(request,"users/registration.html",context)

def viewCart(request):
    orders=Order.objects.filter(user=request.user)
    context={}
    context["orders"]=orders
    return render(request,"users/mycart.html",context)

def removeCart(request,pk):
    orders=Order.objects.get(id=pk).delete()
    return redirect("cart")


def viewDetails(request,pk):
    order=Order.objects.get(id=pk)
    context={}
    context["order"]=order
    return render(request,"users/orderdetails.html",context)
@login_required(login_url="signin")

def orderMobile(request,pk):
    mobile=Mobile.objects.get(id=pk)
    mobilename=mobile.mob_name
    form=OrderForm(initial={'mobile':mobilename,'user':request.user})
    context={}
    context["form"]=form
    if request.method=="POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("cart")
        else:
            form=OrderForm(request.POST)
            context["form"]=form

            return render(request, "users/ordermobile.html", context)

    return render(request,"users/ordermobile.html",context)

def editProfile(request,pk):

    users=User.objects.get(id=pk)
    form = EditProfile(instance=users)
    context = {}
    context["form"] = form
    context["user"]=users
    if request.method == "POST":
        form = EditProfile(instance=users,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context["form"] = form
        return render(request, "user/editpro.html", context)

    return render(request, "users/editpro.html", context)
