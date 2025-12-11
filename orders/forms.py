from django import forms
from accounts.models import City,State

class BuyForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        label="Quantity",
        required=True
    )

    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label="Delivery City",
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    address = forms.CharField(
        max_length=255,
        label="Shipping Address",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    phone = forms.CharField(
        max_length=15,
        label="Phone Number",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )