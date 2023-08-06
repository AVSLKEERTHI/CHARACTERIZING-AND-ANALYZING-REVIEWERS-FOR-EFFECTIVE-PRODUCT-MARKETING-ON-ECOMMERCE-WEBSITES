from user.models import Users, Purchase
from django import forms

class UsersForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    mobile = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Mobile Number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Id'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Location'}))
    class Meta:
        model = Users
        fields = ('firstname', 'lastname', 'username', 'password', 'profession', 'email','mobile','location')

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('quantity',)