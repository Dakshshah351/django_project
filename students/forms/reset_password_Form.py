
from django.contrib.auth.forms import UserCreationForm
from ..models import reset_password_Form
from django import forms

class reset_password_Form(forms.ModelForm):

    class Meta:
        model = reset_password_Form
        fields = ["email"]