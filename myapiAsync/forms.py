from django import forms

class Product(forms.Form):
    product_name = forms.CharField(label='Product Name', required=True)
    product_category = forms.CharField(label='Product Category', required=True)
    product_desc = forms.CharField(label='Product Desc', required=True)