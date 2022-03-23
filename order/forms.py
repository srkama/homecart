from django import forms

class PaymentForm(forms.Form):
    card_number = forms.CharField(required=True)
    cvv2 = forms.CharField(required=True)
    expiry = forms.CharField(required=True)