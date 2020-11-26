from django.forms import ModelForm
from Users.models import Order
from django import forms

from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm

from django.contrib.auth.models import User
class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class SignInForm(AuthenticationForm):
    class Meta:
        model=User
        fields=["username","password"]
class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        widgets = {
            "mobile": forms.TextInput(attrs={'class': 'form-control'}),
            "user": forms.HiddenInput(),
            "quantity": forms.TextInput(attrs={'class': 'form-control'}),
            "Address": forms.TextInput(attrs={'class': 'form-control'}),
            "status": forms.HiddenInput(),

        }

class EditProfile(UserChangeForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username"]



