
from django import forms

class change_pass_Form(forms.Form):
    password = forms.CharField(label="password", max_length=100)
    Confirm_Password = forms.CharField(label="confirm_pass",max_length=100)