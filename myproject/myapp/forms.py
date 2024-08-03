from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    contact_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Contact Number'}))
    department = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Department'}))
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'full_name', 'contact_number', 'department', 'profile_picture']
