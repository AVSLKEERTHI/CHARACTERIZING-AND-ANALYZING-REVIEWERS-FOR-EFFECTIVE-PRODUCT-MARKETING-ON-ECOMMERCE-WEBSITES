from admins.models import Prodcuts
from django import forms

class UploadForm(forms.ModelForm):
    vendor_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Vendor Name'}))
    version_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Product Version Name'}))
    color = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Color Of the Product'}))
    price = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Price'}))
    featuers = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Product Features'}))
    class Meta:
        model = Prodcuts
        fields = ('product_name', 'vendor_name', 'version_name', 'color', 'price', 'featuers', 'images')