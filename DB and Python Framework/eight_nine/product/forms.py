from django import forms
from .models import ProductMst, ProductSubCat

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductMst
        fields = ['product_name']

class ProductSubCatForm(forms.ModelForm):
    class Meta:
        model = ProductSubCat
        fields = ['product', 'price', 'image', 'model', 'ram']
