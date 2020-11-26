from django.shortcuts import render, redirect
from shopowner.forms import BrandCreateForm,UpdateBrand,CreateMobile,MobileUpdate,OrderForm
from shopowner.models import Brand,Mobile
from Users.models import Order
from Users.models import *
# Create your views here.

# def listBrand(request):
#
#     form = BrandCreateForm()
#     context["form"] = form
#     return render(request, "bandcreation.html", context)
def createBrand(request):
    template_name="bandcreation.html"
    form=BrandCreateForm()
    context={}
    brands = Brand.objects.all()
    context["brands"] = brands
    context["form"]=form
    if request.method=="POST":
        form=BrandCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("createbrand")
        else:
            context["form"]=form
            return render(request, template_name, context)

    return render(request,template_name,context)

def viewBrand(request,pk):
    brands=Brand.objects.get(id=pk)
    context={}
    context["brands"]=brands
    template_name="view.html"
    return render(request,template_name,context)
def deleteBrand(request,pk):
    Brand.objects.get(id=pk).delete()
    return redirect("createbrand")

def updateBrand(request,pk):
    brands=Brand.objects.get(id=pk)
    form=UpdateBrand(instance=brands)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UpdateBrand(instance=brands,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("createbrand")
    return render(request,"update.html",context)
def listMobile(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    template_name="listmobile.html"
    return render(request, template_name, context)


def createMobile(request):
    form=CreateMobile()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=CreateMobile(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listmobile")
        else:
            context["form"] = form
            return render(request, "createMob.html", context)

    return render(request,"createMob.html",context)

def mobileView(request,pk):
    mobile=Mobile.objects.get(id=pk)
    context={}
    context["mobile"]=mobile
    template_name="mobview.html"

    return render(request,template_name,context)
def mobileDelete(request,pk):
    Mobile.objects.get(id=pk).delete()
    return redirect("listmobile")

def updateMobile(request,pk):
    mobile = Mobile.objects.get(id=pk)
    form=MobileUpdate(instance=mobile)
    context = {}
    context["mobile"] = mobile
    context["form"]=form
    if request.method=="POST":
        form=MobileUpdate(instance=mobile,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listmobile")
    return render(request,"mobupdate.html",context)

def viewOrders(request):
    orders=Order.objects.all()
    context={}
    context["orders"]=orders
    return render(request,"vieworders.html",context)
def orderdetails(request,pk):
    orders = Order.objects.get(id=pk)
    form=OrderForm(instance=orders)
    context = {}
    context["form"] = form
    if request.method=="POST":
        form=OrderForm(instance=orders,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("vieworders")
    return render(request,"orderdetails.html",context)
def index(request):
    return render(request,"index.html")