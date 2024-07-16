from django import forms


class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=12, required=True, label='Full Name')
    shipping_add = forms.CharField(
        widget=forms.Textarea,
        required=True,
        label='Shipping Address'
        )
    email_adress = forms.EmailField(required=False, label='Email Address')