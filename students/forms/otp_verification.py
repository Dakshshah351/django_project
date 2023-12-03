
from django import forms

class otpForm(forms.Form):
    otp = forms.IntegerField(label="otp", max_length=100)