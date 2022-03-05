from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class UserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name",
                  "password1", "password2")

class UserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("starter", "main", "dessert", "delivery")

class ConformationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("status",)
        
        widgets = {
            'status': forms.TextInput(attrs={'type': 'hidden'}),
        }

class CreateDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ("course", "name", "descrip", "diet", "price")

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("status",)
        
        widgets = {
            'status': forms.TextInput(attrs={'type': 'hidden'}),
        }



 
