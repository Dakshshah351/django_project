
from django.contrib.auth.forms import UserCreationForm
from .. models import adminPanel
from django import forms

class loginform(forms.ModelForm):

    class Meta:
        model = adminPanel
        fields = ('username','password')
        widgets = {
            "password":  forms.PasswordInput,
        }