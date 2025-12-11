from django import forms
from .models import Product, Category
from accounts.models import City,State

class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Product.objects.none())
    available_in = forms.ModelMultipleChoiceField(
        queryset=None, 
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Available in Cities"
    )

    class Meta:
        model = Product
        fields = ['name','description','price','stock','image','category', 'available_in']
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()

        self.fields['available_in'].queryset = City.objects.all()
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock<0:
            raise forms.ValidationError("stock cannot be nagative ")
        return stock

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price