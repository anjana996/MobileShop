from django.forms import ModelForm
from django import forms
from shopowner.models import Brand,Mobile
from Users.forms import Order

class BrandCreateForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets={
            "brand_name":forms.TextInput(attrs={'class':'form-control'}),
        }


    def clean(self):
        print("clean")
        cleaned_data = super().clean()
        brandname = cleaned_data.get("brand_name")
        brand = Brand.objects.filter(brand_name=brandname)

        if brand:
            msg = "Brand with same name already exist"
            self.add_error('brand_name', msg)
class UpdateBrand(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
class CreateMobile(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
        widgets = {
            "mob_name": forms.TextInput(attrs={'class': 'form-control'}),
            "brand":forms.Select(),
            "ram": forms.TextInput(attrs={'class': 'form-control'}),
            "internal": forms.TextInput(attrs={'class': 'form-control'}),
            "color": forms.TextInput(attrs={'class': 'form-control'}),
            "screensize": forms.TextInput(attrs={'class': 'form-control'}),
            "processor": forms.TextInput(attrs={'class': 'form-control'}),
            "price": forms.TextInput(attrs={'class': 'form-control'}),


        }

class MobileUpdate(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
        widgets = {
            "mob_name": forms.TextInput(attrs={'class': 'form-control'}),
            "brand": forms.Select(),
            "ram": forms.TextInput(attrs={'class': 'form-control'}),
            "internal": forms.TextInput(attrs={'class': 'form-control'}),
            "color": forms.TextInput(attrs={'class': 'form-control'}),
            "screensize": forms.TextInput(attrs={'class': 'form-control'}),
            "processor": forms.TextInput(attrs={'class': 'form-control'}),
            "price": forms.TextInput(attrs={'class': 'form-control'}),

        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {
            "mobile": forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            "user": forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            "quantity": forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            "Address": forms.Textarea(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            "status": forms.Select(attrs={'class': 'form-control'})
        }
