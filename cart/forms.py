from django import forms


class CheckoutForm(forms.Form):
    shipping_add = forms.CharField(widget=forms.Textarea, required=True)
