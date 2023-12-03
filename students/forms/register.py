
from django.contrib.auth.forms import UserCreationForm
from .. models import UserModel
from django import forms


class CustomUserCreationForms(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ('username','userProfile','first_name','last_name','email','roll','technology')

class UpdateProfile(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ('username','userProfile','first_name','last_name','email')

class Update(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ('userProfile','first_name','last_name','email')

