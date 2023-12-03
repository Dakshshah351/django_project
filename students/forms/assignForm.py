from django import forms
from ..models import RequirementModel

#creating a form
class assignform(forms.ModelForm):
    #create meta class
    class Meta:
        model = RequirementModel
        fields = [
            "assigned_dev",

        ]