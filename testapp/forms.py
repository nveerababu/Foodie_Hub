from django import forms
from django.contrib.auth.models import User
from testapp.models import MenuItem

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'category', 'price', 'image_path']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item Name'}),
            'category': forms.Select(attrs={'class': 'form-control'}), 
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price in ₹'}),
            'image_path': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'images/mc1.png'}),
        }